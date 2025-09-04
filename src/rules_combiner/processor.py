"""Rule processor for content processing and formatting."""

import re
from pathlib import Path
from typing import List

from .models import RuleFile


class RuleProcessor:
    """Processes and formats rule content for combination.
    
    This class handles reading rule file content, formatting it for inclusion
    in the combined document, and generating supporting elements like table
    of contents.
    
    Example:
        >>> processor = RuleProcessor()
        >>> content = processor.read_rule_content(Path("rule.md"))
        >>> formatted = processor.format_rule_section(content, "My Rule")
    """
    
    def __init__(self) -> None:
        """Initialize the rule processor."""
        pass
    
    def read_rule_content(self, rule_path: Path) -> str:
        """Read and return the content of a rule file.
        
        Reads the file content with UTF-8 encoding and returns it as a string.
        
        Args:
            rule_path: Path to the rule file to read.
            
        Returns:
            The content of the rule file as a string.
            
        Raises:
            FileNotFoundError: If the rule file does not exist.
            UnicodeDecodeError: If the file cannot be decoded as UTF-8.
        """
        try:
            return rule_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"Rule file not found: {rule_path}")
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(
                e.encoding, e.object, e.start, e.end,
                f"Cannot decode rule file {rule_path}: {e.reason}"
            )
    
    def format_rule_section(self, content: str, title: str) -> str:
        """Format rule content as a section in the combined document.
        
        Takes raw rule content and formats it for inclusion in the combined
        document. This includes:
        - Replacing the original title with the provided title
        - Preserving subsection headers (##, ###, etc.)
        - Maintaining original formatting and structure
        
        Args:
            content: Raw content from the rule file.
            title: Title to use for this section.
            
        Returns:
            Formatted content ready for inclusion in combined document.
        """
        if not content.strip():
            # Handle empty content
            return f"# {title}\n\n*No content available.*\n\n"
        
        lines = content.split('\n')
        formatted_lines = []
        first_header_found = False
        
        for line in lines:
            # Check if this is the first level-1 header and replace it
            if line.strip().startswith('# ') and not first_header_found:
                # Replace the first level-1 header with our title
                formatted_lines.append(f"# {title}")
                first_header_found = True
            else:
                # Keep all other content as-is (including subsection headers)
                formatted_lines.append(line)
        
        # If no level-1 header was found, add our title at the beginning
        if not first_header_found:
            formatted_lines.insert(0, f"# {title}")
            formatted_lines.insert(1, "")  # Add empty line after title
        
        # Ensure the section ends with proper spacing
        formatted_content = '\n'.join(formatted_lines)
        if not formatted_content.endswith('\n\n'):
            if formatted_content.endswith('\n'):
                formatted_content += '\n'
            else:
                formatted_content += '\n\n'
        
        return formatted_content
    
    def generate_table_of_contents(self, rules: List[RuleFile]) -> str:
        """Generate a table of contents for the combined rules.
        
        Creates a markdown table of contents with links to each rule section.
        
        Args:
            rules: List of RuleFile objects to include in the TOC.
            
        Returns:
            Formatted table of contents as markdown string.
        """
        if not rules:
            return "# Table of Contents\n\nNo rules selected.\n\n"
        
        toc_lines = ["# Table of Contents", ""]
        
        for i, rule in enumerate(rules, 1):
            # Create anchor-friendly link from title
            anchor = self._create_anchor_link(rule.title)
            toc_lines.append(f"{i}. [{rule.title}](#{anchor})")
        
        toc_lines.append("")  # Add final empty line
        return '\n'.join(toc_lines)
    
    def _create_anchor_link(self, title: str) -> str:
        """Create a GitHub-flavored markdown anchor link from a title.
        
        Converts a title to a valid anchor link by:
        - Converting to lowercase
        - Replacing spaces and special characters with hyphens
        - Removing non-alphanumeric characters except hyphens
        
        Args:
            title: The section title.
            
        Returns:
            Anchor-friendly link string.
        """
        # Convert to lowercase and replace spaces with hyphens
        anchor = title.lower().strip()
        
        # Replace spaces and underscores with hyphens
        anchor = re.sub(r'[\s_]+', '-', anchor)
        
        # Remove special characters except hyphens and alphanumeric
        anchor = re.sub(r'[^a-z0-9\-]', '', anchor)
        
        # Remove multiple consecutive hyphens
        anchor = re.sub(r'-+', '-', anchor)
        
        # Remove leading/trailing hyphens
        anchor = anchor.strip('-')
        
        return anchor
