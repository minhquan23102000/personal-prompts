"""Simplified unit tests for InteractiveSelector."""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from rules_combiner.selector import InteractiveSelector
from rules_combiner.models import RuleFile


@pytest.fixture
def sample_rule_files(tmp_path: Path) -> list[RuleFile]:
    """Create sample rule files for testing."""
    files = []
    for i in range(1, 4):
        file_path = tmp_path / f"test{i}.md"
        file_path.write_text(f"# Test Rule {i}\nThis is test rule {i}.")
        rule_file = RuleFile(file_path, f"test{i}.md", f"Test Rule {i}")
        files.append(rule_file)
    return files


class TestInteractiveSelector:
    """Test cases for InteractiveSelector."""

    def test_initialization(self, sample_rule_files: list[RuleFile]) -> None:
        """Test creating an InteractiveSelector."""
        # Act
        selector = InteractiveSelector(sample_rule_files)
        
        # Assert
        assert selector._rules == sample_rule_files
        assert selector._console is not None

    def test_initialization_with_empty_list(self) -> None:
        """Test creating an InteractiveSelector with empty rules."""
        # Act
        selector = InteractiveSelector([])
        
        # Assert
        assert selector._rules == []

    def test_parse_selection_input_single_numbers(self, sample_rule_files: list[RuleFile]) -> None:
        """Test parsing single numbers."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        indices = selector._parse_selection_input("1,3")
        
        # Assert
        assert indices == [0, 2]  # 1-based to 0-based

    def test_parse_selection_input_ranges(self, sample_rule_files: list[RuleFile]) -> None:
        """Test parsing ranges."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        indices = selector._parse_selection_input("1-3")
        
        # Assert
        assert indices == [0, 1, 2]

    def test_parse_selection_input_all(self, sample_rule_files: list[RuleFile]) -> None:
        """Test parsing 'all' keyword."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        indices = selector._parse_selection_input("all")
        
        # Assert
        assert indices == [0, 1, 2]

    def test_parse_selection_input_invalid(self, sample_rule_files: list[RuleFile]) -> None:
        """Test parsing invalid input raises ValueError."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act & Assert
        with pytest.raises(ValueError):
            selector._parse_selection_input("invalid")
        
        with pytest.raises(ValueError):
            selector._parse_selection_input("0")  # 0 is invalid
        
        with pytest.raises(ValueError):
            selector._parse_selection_input("99")  # Out of range

    @patch('builtins.input', return_value='y')
    def test_confirm_selection_yes(self, mock_input: Mock, sample_rule_files: list[RuleFile]) -> None:
        """Test confirming selection with yes."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        result = selector.confirm_selection(["test1.md"])
        
        # Assert
        assert result is True

    @patch('builtins.input', return_value='n')
    def test_confirm_selection_no(self, mock_input: Mock, sample_rule_files: list[RuleFile]) -> None:
        """Test confirming selection with no."""
        # Arrange
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        result = selector.confirm_selection(["test1.md"])
        
        # Assert
        assert result is False

    @patch('rules_combiner.selector.Console')
    def test_display_rules(self, mock_console_class: MagicMock, sample_rule_files: list[RuleFile]) -> None:
        """Test displaying rules."""
        # Arrange
        mock_console = MagicMock()
        mock_console_class.return_value = mock_console
        selector = InteractiveSelector(sample_rule_files)
        
        # Act
        selector.display_rules()
        
        # Assert
        mock_console.print.assert_called()  # Should call print at least once
