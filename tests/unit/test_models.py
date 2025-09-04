"""Unit tests for core data models."""

import pytest
from pathlib import Path
from pydantic import ValidationError

from rules_combiner.models import RuleFile, CombinationConfig, SelectionMode


class TestRuleFile:
    """Test cases for RuleFile data model."""

    def test_rule_file_creation_with_valid_path(self, tmp_path: Path) -> None:
        """Test creating a RuleFile with a valid file path."""
        # Arrange
        test_file = tmp_path / "test_rule.md"
        test_content = "# Test Rule\nThis is a test rule."
        test_file.write_text(test_content)
        
        # Act
        rule_file = RuleFile(
            path=test_file,
            filename="test_rule.md",
            title="Test Rule",
            file_size=len(test_content)
        )
        
        # Assert
        assert rule_file.path == test_file
        assert rule_file.filename == "test_rule.md"
        assert rule_file.title == "Test Rule"
        assert rule_file.description is None
        assert rule_file.file_size == len(test_content)
        assert rule_file.is_readable is True
        assert rule_file.estimated_tokens == len(test_content) // 4

    def test_rule_file_creation_with_nonexistent_path(self) -> None:
        """Test creating a RuleFile with a non-existent file path raises ValueError."""
        # Arrange
        nonexistent_path = Path("/nonexistent/file.md")
        
        # Act & Assert
        with pytest.raises(ValueError, match="Rule file does not exist"):
            RuleFile(
                path=nonexistent_path,
                filename="file.md",
                title="Nonexistent Rule"
            )

    def test_rule_file_creation_with_directory_path(self, tmp_path: Path) -> None:
        """Test creating a RuleFile with a directory path raises ValueError."""
        # Arrange
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()
        
        # Act & Assert
        with pytest.raises(ValueError, match="Path is not a file"):
            RuleFile(
                path=test_dir,
                filename="test_dir",
                title="Directory Rule"
            )

    def test_rule_file_with_optional_fields(self, tmp_path: Path) -> None:
        """Test creating a RuleFile with all optional fields."""
        # Arrange
        test_file = tmp_path / "detailed_rule.md"
        test_content = "# Detailed Rule\nThis is a detailed test rule with description."
        test_file.write_text(test_content)
        
        # Act
        rule_file = RuleFile(
            path=test_file,
            filename="detailed_rule.md",
            title="Detailed Rule",
            description="This is a detailed test rule with description.",
            file_size=len(test_content),
            is_readable=True
        )
        
        # Assert
        assert rule_file.description == "This is a detailed test rule with description."
        assert rule_file.file_size == len(test_content)
        assert rule_file.is_readable is True
        assert rule_file.estimated_tokens == len(test_content) // 4

    def test_token_estimation(self, tmp_path: Path) -> None:
        """Test token estimation functionality."""
        # Arrange
        test_file = tmp_path / "token_test.md"
        # Create content with known character count
        test_content = "x" * 400  # 400 characters should be ~100 tokens
        test_file.write_text(test_content)
        
        # Act
        rule_file = RuleFile(
            path=test_file,
            filename="token_test.md",
            title="Token Test",
            file_size=len(test_content)
        )
        
        # Assert
        assert rule_file.estimated_tokens == 100  # 400 / 4 = 100
        assert rule_file.estimate_tokens_from_file_size() == 100

    def test_token_estimation_minimum(self, tmp_path: Path) -> None:
        """Test that token estimation has a minimum of 1."""
        # Arrange
        test_file = tmp_path / "tiny.md"
        test_file.write_text("x")  # 1 character
        
        # Act
        rule_file = RuleFile(
            path=test_file,
            filename="tiny.md", 
            title="Tiny Rule",
            file_size=1
        )
        
        # Assert
        assert rule_file.estimated_tokens == 1  # Should be at least 1


class TestSelectionMode:
    """Test cases for SelectionMode enum."""

    def test_selection_mode_values(self) -> None:
        """Test that SelectionMode has expected values."""
        # Assert
        assert SelectionMode.INTERACTIVE.value == "interactive"
        assert SelectionMode.ALL.value == "all"
        assert SelectionMode.SPECIFIC.value == "specific"

    def test_selection_mode_members(self) -> None:
        """Test that SelectionMode has expected members."""
        # Assert
        assert len(SelectionMode) == 3
        assert SelectionMode.INTERACTIVE in SelectionMode
        assert SelectionMode.ALL in SelectionMode
        assert SelectionMode.SPECIFIC in SelectionMode


class TestCombinationConfig:
    """Test cases for CombinationConfig data model."""

    def test_combination_config_creation_with_valid_paths(self, tmp_path: Path) -> None:
        """Test creating a CombinationConfig with valid paths."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        output_file = tmp_path / "AGENT.md"
        selected_rules = ["rule1.md", "rule2.md"]
        
        # Act
        config = CombinationConfig(
            rules_directory=rules_dir,
            output_file=output_file,
            selected_rules=selected_rules
        )
        
        # Assert
        assert config.rules_directory == rules_dir
        assert config.output_file == output_file
        assert config.selected_rules == selected_rules
        assert config.include_toc is True
        assert config.backup_existing is True

    def test_combination_config_creation_with_nonexistent_rules_dir(self, tmp_path: Path) -> None:
        """Test creating a CombinationConfig with non-existent rules directory raises ValueError."""
        # Arrange
        nonexistent_dir = tmp_path / "nonexistent"
        output_file = tmp_path / "AGENT.md"
        selected_rules = ["rule1.md"]
        
        # Act & Assert
        with pytest.raises(ValueError, match="Rules directory does not exist"):
            CombinationConfig(
                rules_directory=nonexistent_dir,
                output_file=output_file,
                selected_rules=selected_rules
            )

    def test_combination_config_creation_with_file_as_rules_dir(self, tmp_path: Path) -> None:
        """Test creating a CombinationConfig with a file as rules directory raises ValueError."""
        # Arrange
        rules_file = tmp_path / "rules.txt"
        rules_file.write_text("not a directory")
        output_file = tmp_path / "AGENT.md"
        selected_rules = ["rule1.md"]
        
        # Act & Assert
        with pytest.raises(ValueError, match="Path is not a directory"):
            CombinationConfig(
                rules_directory=rules_file,
                output_file=output_file,
                selected_rules=selected_rules
            )

    def test_combination_config_with_custom_options(self, tmp_path: Path) -> None:
        """Test creating a CombinationConfig with custom options."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        output_file = tmp_path / "AGENT.md"
        selected_rules = ["rule1.md", "rule2.md", "rule3.md"]
        
        # Act
        config = CombinationConfig(
            rules_directory=rules_dir,
            output_file=output_file,
            selected_rules=selected_rules,
            include_toc=False,
            backup_existing=False
        )
        
        # Assert
        assert config.include_toc is False
        assert config.backup_existing is False
