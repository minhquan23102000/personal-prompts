"""Rule discovery engine for finding and cataloging rule files."""

import re
from pathlib import Path
from typing import List

from loguru import logger

from .models import RuleFile


class RuleDiscoveryEngine:
    """Discovers and catalogs rule files in the rules directory.
    
    This class provides functionality to scan a directory for Markdown files,
    validate their accessibility, extract metadata like titles, and return
    structured information about available rule files.
    
    Example:
        >>> engine = RuleDiscoveryEngine(Path("rules"))
        >>> rules = engine.discover_rules()
        >>> for rule in rules:
        ...     print(f"{rule.filename}: {rule.title}")
    """
    
    def __init__(self, rules_dir: Path) -> None:
        """Initialize the discovery engine with rules directory path.
        
        Args:
            rules_dir: Path to the directory containing rule files.
        """
        self._rules_dir = rules_dir
        self._logger = logger.bind(component="discovery")
    
    def discover_rules(self) -> List[RuleFile]:
        """Discover all valid rule files in the directory.
        
        Scans the rules directory for .md files, validates each file,
        and returns a list of RuleFile objects with extracted metadata.
        
        Returns:
            List of RuleFile objects representing valid rule files found.
            
        Example:
            >>> engine = RuleDiscoveryEngine(Path("rules"))
            >>> rules = engine.discover_rules()
            >>> len(rules)  # Number of valid rule files found
        """
        self._logger.info(f"Starting rule discovery in: {self._rules_dir}")
        
        discovered_rules: List[RuleFile] = []
        
        # Find all .md files in the rules directory (not recursive)
        markdown_files = list(self._rules_dir.glob("*.md"))
        
        self._logger.info(f"Found {len(markdown_files)} markdown files to process")
        
        for md_file in markdown_files:
            if self.validate_rule_file(md_file):
                try:
                    title = self.extract_title(md_file)
                    file_size = md_file.stat().st_size
                    # Estimate tokens: ~4 characters = 1 token
                    estimated_tokens = max(1, file_size // 4)
                    
                    rule_file = RuleFile(
                        path=md_file,
                        filename=md_file.name,
                        title=title,
                        file_size=file_size,
                        is_readable=True,
                        estimated_tokens=estimated_tokens
                    )
                    
                    discovered_rules.append(rule_file)
                    self._logger.debug(f"Added rule file: {md_file.name} (title: '{title}')")
                    
                except Exception as e:
                    self._logger.warning(f"Failed to process rule file {md_file.name}: {e}")
        
        self._logger.info(f"Successfully discovered {len(discovered_rules)} rule files")
        return discovered_rules
    
    def validate_rule_file(self, file_path: Path) -> bool:
        """Validate that a file is a readable rule file.
        
        Checks if the file exists, is a regular file, and can be read.
        
        Args:
            file_path: Path to the file to validate.
            
        Returns:
            True if the file is valid and readable, False otherwise.
        """
        try:
            if not file_path.exists():
                self._logger.debug(f"File does not exist: {file_path}")
                return False
                
            if not file_path.is_file():
                self._logger.debug(f"Path is not a file: {file_path}")
                return False
            
            # Test if we can read the file
            file_path.read_text(encoding='utf-8')
            return True
            
        except (PermissionError, UnicodeDecodeError, OSError) as e:
            self._logger.debug(f"Cannot read file {file_path}: {e}")
            return False
    
    def extract_title(self, file_path: Path) -> str:
        """Extract the title from the first header in the markdown file.
        
        Looks for the first level-1 markdown header (line starting with '# ')
        and returns the text after the hash. If no header is found, returns
        the filename without extension.
        
        Args:
            file_path: Path to the markdown file.
            
        Returns:
            The extracted title or filename as fallback.
            
        Example:
            For a file containing \"# Mental Model: Test Rule\", returns
            \"Mental Model: Test Rule\".
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Look for the first level-1 header (# Title)
            # Match lines that start with # followed by space and capture until end of line
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('# '):
                    title = line[2:].strip()  # Remove '# ' and any extra whitespace
                    self._logger.debug(f"Extracted title from {file_path.name}: '{title}'")
                    return title
            
            # Use filename without extension as fallback
            fallback_title = file_path.stem
            self._logger.debug(f"No header found in {file_path.name}, using filename: '{fallback_title}'")
            return fallback_title
                
        except (UnicodeDecodeError, OSError) as e:
            self._logger.warning(f"Could not read file {file_path.name} for title extraction: {e}")
            return file_path.stem
