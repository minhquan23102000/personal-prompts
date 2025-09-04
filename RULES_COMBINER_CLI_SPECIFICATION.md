# Technical Specification: Rules Combiner CLI

## Executive Summary

This document specifies the requirements, design, and implementation plan for a Python CLI tool that combines multiple rule files from the `rules/` directory into a single consolidated `AGENT.md` file. The tool provides an interactive selection interface and maintains proper formatting throughout the combination process.

## 1. Project Foundations

### 1.1 Problem Statement

The user maintains multiple rule files in a `rules/` directory, each containing different mental models and constraints for AI agents. Currently, there's no efficient way to combine selected rules into a single, consolidated file for easier management and deployment.

### 1.2 Project Goals

- **Primary Goal**: Create a Python CLI tool that can discover, select, and combine rule files
- **Secondary Goals**: 
  - Provide intuitive interactive selection interface
  - Maintain original formatting and readability
  - Follow modern Python development practices
  - Ensure cross-platform compatibility

### 1.3 Success Criteria

1. ✅ CLI tool successfully lists all `.md` files from the `rules/` directory
2. ✅ Interactive selection mechanism allows users to choose multiple rules
3. ✅ Combined output file preserves original formatting and adds proper section headers
4. ✅ Tool follows modern Python best practices with proper error handling and type annotations
5. ✅ Output file is named `AGENT.md` and placed in the project root
6. ✅ Tool provides clear feedback and error messages to users

### 1.4 Constraints and Assumptions

**Technical Constraints:**
- Must be a command-line interface (CLI) application
- Must work with existing file structure (`rules/` folder)
- Output file must be named `AGENT.md`
- Must maintain compatibility with Windows PowerShell environment

**Assumptions:**
- Rule files are in Markdown format (`.md` extension)
- Files are UTF-8 encoded
- User has read/write permissions for the project directory

## 2. Functional Decomposition

### 2.1 Vertical Slices

The application is decomposed into five independent, end-to-end functional units:

#### Slice 1: Rule Discovery Engine
**Purpose**: Scan and catalog available rule files
- Discover all `.md` files in `rules/` directory
- Extract metadata (filename, title, description)
- Validate file accessibility and readability
- Return structured list of available rules

#### Slice 2: Interactive Selection Interface
**Purpose**: Enable user to select multiple rules for combination
- Display available rules in user-friendly format
- Provide checkbox-style multi-selection interface
- Handle input validation and selection confirmation
- Support "select all" and "clear all" operations

#### Slice 3: Rule Content Processor
**Purpose**: Process selected rule files for combination
- Read selected rule files and extract content
- Maintain original formatting and structure
- Add consistent section headers and separators
- Handle encoding issues and special characters

#### Slice 4: Output File Generator
**Purpose**: Create the final combined rules file
- Combine processed rule content into single document
- Generate proper markdown structure with table of contents
- Write output to `AGENT.md` with atomic operations
- Handle file write permissions and backup existing files

#### Slice 5: CLI Framework & Error Handling
**Purpose**: Provide robust command-line interface
- Implement command-line argument parsing
- Provide comprehensive help documentation
- Implement error handling and user feedback
- Add structured logging for debugging

## 3. Technical Architecture

### 3.1 Core Data Models

```python
from dataclasses import dataclass
from pathlib import Path
from enum import Enum
from typing import List, Optional

@dataclass
class RuleFile:
    """Represents a single rule file with metadata."""
    path: Path
    filename: str
    title: str
    description: Optional[str] = None
    file_size: int = 0
    is_readable: bool = True

    def __post_init__(self) -> None:
        """Validate the rule file after initialization."""
        if not self.path.exists():
            raise ValueError(f"Rule file does not exist: {self.path}")
        if not self.path.is_file():
            raise ValueError(f"Path is not a file: {self.path}")

class SelectionMode(Enum):
    """Enumeration of selection modes for the CLI."""
    INTERACTIVE = "interactive"
    ALL = "all"
    SPECIFIC = "specific"

@dataclass
class CombinationConfig:
    """Configuration for the rule combination process."""
    rules_directory: Path
    output_file: Path
    selected_rules: List[str]
    include_toc: bool = True
    backup_existing: bool = True
    
    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if not self.rules_directory.exists():
            raise ValueError(f"Rules directory does not exist: {self.rules_directory}")
        if not self.rules_directory.is_dir():
            raise ValueError(f"Path is not a directory: {self.rules_directory}")
```

### 3.2 Core Classes and Interfaces

#### 3.2.1 RuleDiscoveryEngine

```python
class RuleDiscoveryEngine:
    """Discovers and catalogs rule files in the rules directory."""
    
    def __init__(self, rules_dir: Path) -> None:
        """Initialize the discovery engine with rules directory path."""
        self._rules_dir = rules_dir
        self._logger = logger.bind(component="discovery")
    
    def discover_rules(self) -> List[RuleFile]:
        """Discover all valid rule files in the directory."""
        
    def validate_rule_file(self, file_path: Path) -> bool:
        """Validate that a file is a readable rule file."""
        
    def extract_title(self, file_path: Path) -> str:
        """Extract the title from the first header in the markdown file."""
```

#### 3.2.2 InteractiveSelector

```python
class InteractiveSelector:
    """Provides interactive selection interface for rules."""
    
    def __init__(self, available_rules: List[RuleFile]) -> None:
        """Initialize selector with available rule files."""
        self._rules = available_rules
        self._console = Console()
    
    def display_rules(self) -> None:
        """Display available rules in a formatted table."""
        
    def get_user_selection(self) -> List[str]:
        """Get user selection through interactive prompts."""
        
    def confirm_selection(self, selected: List[str]) -> bool:
        """Confirm the user's selection before proceeding."""
```

#### 3.2.3 RuleProcessor

```python
class RuleProcessor:
    """Processes and formats rule content for combination."""
    
    def read_rule_content(self, rule_path: Path) -> str:
        """Read and return the content of a rule file."""
        
    def format_rule_section(self, content: str, title: str) -> str:
        """Format rule content as a section in the combined document."""
        
    def generate_table_of_contents(self, rules: List[RuleFile]) -> str:
        """Generate a table of contents for the combined rules."""
```

#### 3.2.4 OutputGenerator

```python
class OutputGenerator:
    """Generates the final combined rules file."""
    
    def __init__(self, output_path: Path, backup: bool = True) -> None:
        """Initialize generator with output path and backup preference."""
        self._output_path = output_path
        self._backup_enabled = backup
    
    def backup_existing_file(self) -> Optional[Path]:
        """Create a backup of the existing output file if it exists."""
        
    def write_combined_rules(self, content: str) -> None:
        """Write the combined rules content to the output file."""
        
    def validate_output(self) -> bool:
        """Validate that the output file was written correctly."""
```

### 3.3 CLI Interface Design

```python
import click
from rich.console import Console
from pathlib import Path

@click.group()
@click.version_option()
def cli() -> None:
    """Rules Combiner CLI - Combine rule files into a single AGENT.md file."""
    pass

@cli.command()
@click.option(
    "--rules-dir", 
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default="rules",
    help="Directory containing rule files (default: rules)"
)
@click.option(
    "--output", 
    type=click.Path(path_type=Path),
    default="AGENT.md",
    help="Output file name (default: AGENT.md)"
)
@click.option(
    "--no-backup", 
    is_flag=True,
    help="Skip backing up existing output file"
)
@click.option(
    "--no-toc", 
    is_flag=True,
    help="Skip generating table of contents"
)
def generate(rules_dir: Path, output: Path, no_backup: bool, no_toc: bool) -> None:
    """Generate combined rules file interactively."""
    pass

@cli.command()
@click.option(
    "--rules-dir", 
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default="rules"
)
def list_rules(rules_dir: Path) -> None:
    """List all available rule files."""
    pass
```

## 4. Implementation Plan

### 4.1 Development Phases

#### Phase 1: Project Setup (Steps 1-4)
- Create project structure with `src/`, `tests/`, `docs/` directories
- Configure `pyproject.toml` with dependencies (click, rich, loguru, pydantic)
- Initialize git repository with appropriate `.gitignore`
- Set up development tools (pre-commit hooks, linting, formatting)

#### Phase 2: Core Data Models (Steps 5-8)
- Implement `RuleFile` dataclass with Pydantic validation
- Implement `CombinationConfig` dataclass with path validation
- Create `SelectionMode` enum for CLI modes
- Write comprehensive unit tests for all data models

#### Phase 3: Rule Discovery (Steps 9-13)
- Implement `RuleDiscoveryEngine` class with directory scanning
- Add file validation and metadata extraction capabilities
- Implement title extraction from markdown headers
- Create comprehensive tests including edge cases

#### Phase 4: Interactive Interface (Steps 14-18)
- Implement `InteractiveSelector` with Rich formatting
- Add multi-select checkbox interface
- Implement selection confirmation and validation
- Test interactive components with mocked user input

#### Phase 5: Content Processing (Steps 19-22)
- Implement `RuleProcessor` for content reading and formatting
- Add markdown section formatting capabilities
- Implement table of contents generation
- Test content processing with various markdown formats

#### Phase 6: Output Generation (Steps 23-27)
- Implement `OutputGenerator` with atomic file operations
- Add backup functionality with timestamp naming
- Implement output validation and error handling
- Test file operations across different scenarios

#### Phase 7: CLI Integration (Steps 28-32)
- Create main CLI entry point using Click framework
- Implement all command-line arguments and options
- Add comprehensive help documentation
- Integrate structured logging with Loguru

#### Phase 8: Error Handling (Steps 33-36)
- Implement comprehensive exception handling
- Add input validation for all user inputs
- Create informative error messages
- Test error scenarios and edge cases

#### Phase 9: Documentation (Steps 37-40)
- Create detailed README with usage examples
- Add docstrings to all public methods and classes
- Achieve >85% test coverage
- Perform end-to-end testing on target environment

### 4.2 Dependency Requirements

```toml
[tool.poetry.dependencies]
python = "^3.9"
click = "^8.1.0"
rich = "^13.0.0"
loguru = "^0.7.0"
pydantic = "^2.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
pytest-cov = "^4.0.0"
black = "^23.0.0"
isort = "^5.0.0"
mypy = "^1.0.0"
pre-commit = "^3.0.0"
```

## 5. Testing Strategy

### 5.1 Test Categories

#### Unit Tests
- Test individual methods and functions in isolation
- Use mocks for external dependencies (file system, user input)
- Focus on business logic and edge cases
- Target: >90% coverage for core business logic

#### Integration Tests
- Test complete workflows from input to output
- Use temporary directories for file system operations
- Test CLI argument parsing and command execution
- Validate end-to-end functionality

#### File System Tests
- Test actual file operations with real files
- Validate encoding handling and special characters
- Test permission errors and disk space issues
- Use temporary directories to avoid side effects

#### Error Handling Tests
- Test all error conditions and exception paths
- Validate error messages and user guidance
- Test recovery mechanisms where applicable
- Ensure graceful degradation

### 5.2 Test Structure

```
tests/
├── unit/
│   ├── test_rule_discovery.py
│   ├── test_interactive_selector.py
│   ├── test_rule_processor.py
│   ├── test_output_generator.py
│   └── test_data_models.py
├── integration/
│   ├── test_cli_commands.py
│   ├── test_full_workflow.py
│   └── test_error_scenarios.py
├── fixtures/
│   ├── sample_rules/
│   └── test_data.py
└── conftest.py
```

## 6. Risk Analysis and Mitigation

### 6.1 Technical Risks

| Risk | Impact | Probability | Mitigation Strategy |
|------|---------|-------------|-------------------|
| File encoding issues | High | Medium | Implement robust encoding detection and fallback mechanisms |
| Large file handling | Medium | Low | Add file size limits and streaming for large files |
| Concurrent access | Medium | Low | Implement file locking and atomic operations |
| Cross-platform compatibility | High | Medium | Use pathlib, test on multiple platforms |

### 6.2 User Experience Risks

| Risk | Impact | Probability | Mitigation Strategy |
|------|---------|-------------|-------------------|
| Confusing interface | High | Medium | Extensive user testing and intuitive design |
| Data loss | High | Low | Automatic backups and confirmation prompts |
| Poor error messages | Medium | High | Clear, actionable error messages with guidance |

## 7. Quality Assurance Criteria

### 7.1 Code Quality Standards

- **Type Safety**: 100% of public APIs must have type annotations
- **Documentation**: All public classes and methods must have docstrings
- **Test Coverage**: Minimum 85% overall, 90% for core business logic
- **Code Style**: Enforce with Black, isort, and mypy
- **Security**: No hardcoded credentials or unsafe file operations

### 7.2 Performance Requirements

- **Startup Time**: CLI should start within 500ms
- **File Processing**: Handle up to 50 rule files efficiently
- **Memory Usage**: Keep memory footprint under 100MB
- **Output Generation**: Complete within 5 seconds for typical workloads

### 7.3 Usability Requirements

- **Learning Curve**: New users should be productive within 5 minutes
- **Error Recovery**: Clear guidance for all error conditions
- **Help System**: Comprehensive help available via `--help`
- **Feedback**: Progress indication for long-running operations

## 8. Deployment and Maintenance

### 8.1 Installation Methods

- **Development**: `pip install -e .` from source
- **End User**: `pip install rules-combiner-cli` (if published to PyPI)
- **Standalone**: PyInstaller executable for distribution

### 8.2 Configuration Management

- Default configuration embedded in application
- Support for configuration files (optional)
- Environment variable support for CI/CD integration
- Command-line arguments take precedence

### 8.3 Maintenance Considerations

- **Logging**: Structured logging for debugging and audit trails
- **Monitoring**: Track usage patterns and error rates
- **Updates**: Semantic versioning and clear changelog
- **Support**: Issue templates and troubleshooting guide

## 9. Conclusion

This specification provides a comprehensive plan for implementing a robust, user-friendly CLI tool for combining rule files. The design emphasizes simplicity, reliability, and maintainability while following modern Python development practices. The phased implementation approach ensures steady progress with working functionality at each milestone.

The tool will significantly improve the user's workflow for managing and deploying AI agent rules, reducing manual effort and potential errors while maintaining the quality and structure of the original rule files.
