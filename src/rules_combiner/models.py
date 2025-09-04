"""Core data models for the rules combiner CLI."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional


class SelectionMode(Enum):
    """Enumeration of selection modes for the CLI."""
    
    INTERACTIVE = "interactive"
    ALL = "all" 
    SPECIFIC = "specific"


@dataclass
class RuleFile:
    """Represents a single rule file with metadata.
    
    This class encapsulates all the metadata for a rule file including
    its path, basic file information, and content metadata like title
    and description.
    
    Example:
        >>> rule = RuleFile(
        ...     path=Path("rules/test.md"),
        ...     filename="test.md", 
        ...     title="Test Rule"
        ... )
        >>> rule.title
        'Test Rule'
        >>> rule.estimated_tokens
        150
    """
    
    path: Path
    filename: str
    title: str
    description: Optional[str] = None
    file_size: int = 0
    is_readable: bool = True
    estimated_tokens: int = 0
    
    def __post_init__(self) -> None:
        """Validate the rule file after initialization.
        
        Raises:
            ValueError: If the file does not exist or is not a regular file.
        """
        if not self.path.exists():
            raise ValueError(f"Rule file does not exist: {self.path}")
        if not self.path.is_file():
            raise ValueError(f"Path is not a file: {self.path}")
            
        # Auto-calculate estimated tokens if not provided and file is readable
        if self.estimated_tokens == 0 and self.file_size > 0:
            self.estimated_tokens = self.estimate_tokens_from_file_size()
    
    def estimate_tokens_from_file_size(self) -> int:
        """Estimate token count based on file size.
        
        Uses the approximation that ~4 characters = 1 token.
        This is a rough estimate commonly used for OpenAI models.
        
        Returns:
            Estimated number of tokens.
        """
        return max(1, self.file_size // 4)


@dataclass 
class CombinationConfig:
    """Configuration for the rule combination process.
    
    This class holds all the configuration needed to combine rule files,
    including input/output paths, selected rules, and formatting options.
    
    Example:
        >>> config = CombinationConfig(
        ...     rules_directory=Path("rules"),
        ...     output_file=Path("AGENT.md"), 
        ...     selected_rules=["rule1.md", "rule2.md"]
        ... )
        >>> len(config.selected_rules)
        2
    """
    
    rules_directory: Path
    output_file: Path
    selected_rules: List[str]
    include_toc: bool = True
    backup_existing: bool = True
    
    def __post_init__(self) -> None:
        """Validate configuration after initialization.
        
        Raises:
            ValueError: If the rules directory does not exist or is not a directory.
        """
        if not self.rules_directory.exists():
            raise ValueError(f"Rules directory does not exist: {self.rules_directory}")
        if not self.rules_directory.is_dir():
            raise ValueError(f"Path is not a directory: {self.rules_directory}")
