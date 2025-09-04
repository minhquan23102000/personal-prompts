"""Unit tests for RuleDiscoveryEngine."""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from rules_combiner.discovery import RuleDiscoveryEngine
from rules_combiner.models import RuleFile


class TestRuleDiscoveryEngine:
    """Test cases for RuleDiscoveryEngine."""

    def test_rule_discovery_engine_initialization(self, tmp_path: Path) -> None:
        """Test creating a RuleDiscoveryEngine with valid directory."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        # Act
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Assert
        assert engine._rules_dir == rules_dir

    def test_discover_rules_with_empty_directory(self, tmp_path: Path) -> None:
        """Test discovering rules in an empty directory returns empty list."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        rules = engine.discover_rules()
        
        # Assert
        assert rules == []

    def test_discover_rules_with_markdown_files(self, tmp_path: Path) -> None:
        """Test discovering rules with markdown files in directory."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        # Create test markdown files
        (rules_dir / "rule1.md").write_text("# Rule 1\nThis is rule 1.")
        (rules_dir / "rule2.md").write_text("# Rule 2\nThis is rule 2.")
        (rules_dir / "not_rule.txt").write_text("This is not a markdown file.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        rules = engine.discover_rules()
        
        # Assert
        assert len(rules) == 2
        assert all(isinstance(rule, RuleFile) for rule in rules)
        filenames = [rule.filename for rule in rules]
        assert "rule1.md" in filenames
        assert "rule2.md" in filenames
        assert "not_rule.txt" not in filenames

    def test_discover_rules_with_subdirectories(self, tmp_path: Path) -> None:
        """Test that discover_rules ignores subdirectories."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        # Create markdown file in root
        (rules_dir / "root_rule.md").write_text("# Root Rule\nThis is a root rule.")
        
        # Create subdirectory with markdown file
        subdir = rules_dir / "subdir"
        subdir.mkdir()
        (subdir / "sub_rule.md").write_text("# Sub Rule\nThis is a sub rule.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        rules = engine.discover_rules()
        
        # Assert
        assert len(rules) == 1
        assert rules[0].filename == "root_rule.md"

    def test_validate_rule_file_with_valid_file(self, tmp_path: Path) -> None:
        """Test validating a valid markdown file returns True."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "test.md"
        test_file.write_text("# Test Rule\nThis is a test.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        result = engine.validate_rule_file(test_file)
        
        # Assert
        assert result is True

    def test_validate_rule_file_with_nonexistent_file(self, tmp_path: Path) -> None:
        """Test validating a non-existent file returns False."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        nonexistent_file = rules_dir / "nonexistent.md"
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        result = engine.validate_rule_file(nonexistent_file)
        
        # Assert
        assert result is False

    def test_validate_rule_file_with_directory(self, tmp_path: Path) -> None:
        """Test validating a directory returns False."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_dir = rules_dir / "test_dir"
        test_dir.mkdir()
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        result = engine.validate_rule_file(test_dir)
        
        # Assert
        assert result is False

    def test_validate_rule_file_with_unreadable_file(self, tmp_path: Path) -> None:
        """Test validating an unreadable file returns False."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "test.md"
        test_file.write_text("# Test Rule\nThis is a test.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        with patch('pathlib.Path.read_text', side_effect=PermissionError("Access denied")):
            result = engine.validate_rule_file(test_file)
        
        # Assert
        assert result is False

    def test_extract_title_from_valid_markdown(self, tmp_path: Path) -> None:
        """Test extracting title from valid markdown file with header."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "test.md"
        test_file.write_text("# Mental Model: Test Rule\n\nThis is the content.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        title = engine.extract_title(test_file)
        
        # Assert
        assert title == "Mental Model: Test Rule"

    def test_extract_title_from_markdown_without_header(self, tmp_path: Path) -> None:
        """Test extracting title from markdown file without header uses filename."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "no_header.md"
        test_file.write_text("This file has no header.\n\nJust content.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        title = engine.extract_title(test_file)
        
        # Assert
        assert title == "no_header"

    def test_extract_title_from_markdown_with_multiple_headers(self, tmp_path: Path) -> None:
        """Test extracting title uses first header found."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "multiple_headers.md"
        test_file.write_text("# First Header\n\n## Second Header\n\n### Third Header")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        title = engine.extract_title(test_file)
        
        # Assert
        assert title == "First Header"

    def test_extract_title_with_read_error(self, tmp_path: Path) -> None:
        """Test extracting title when file cannot be read uses filename."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        test_file = rules_dir / "unreadable.md"
        test_file.write_text("# Test Header")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        with patch('pathlib.Path.read_text', side_effect=UnicodeDecodeError('utf-8', b'', 0, 1, 'invalid')):
            title = engine.extract_title(test_file)
        
        # Assert
        assert title == "unreadable"

    def test_discover_rules_logs_discovery_count(self, tmp_path: Path) -> None:
        """Test that discover_rules successfully processes files."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        (rules_dir / "valid.md").write_text("# Valid Rule\nContent.")
        
        engine = RuleDiscoveryEngine(rules_dir)
        
        # Act
        rules = engine.discover_rules()
        
        # Assert
        assert len(rules) == 1
        assert rules[0].title == "Valid Rule"
        assert rules[0].filename == "valid.md"
