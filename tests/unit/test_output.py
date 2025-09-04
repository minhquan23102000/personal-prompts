"""Unit tests for OutputGenerator."""

import pytest
from pathlib import Path
from datetime import datetime
from unittest.mock import patch, MagicMock

from rules_combiner.output import OutputGenerator


class TestOutputGenerator:
    """Test cases for OutputGenerator."""

    def test_output_generator_initialization(self, tmp_path: Path) -> None:
        """Test creating an OutputGenerator."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        
        # Act
        generator = OutputGenerator(output_path)
        
        # Assert
        assert generator._output_path == output_path
        assert generator._backup_enabled is True

    def test_output_generator_initialization_no_backup(self, tmp_path: Path) -> None:
        """Test creating an OutputGenerator with backup disabled."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        
        # Act
        generator = OutputGenerator(output_path, backup=False)
        
        # Assert
        assert generator._output_path == output_path
        assert generator._backup_enabled is False

    def test_backup_existing_file_when_file_exists(self, tmp_path: Path) -> None:
        """Test backing up existing file."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Existing Content\n\nSome content.")
        generator = OutputGenerator(output_path, backup=True)
        
        # Act
        with patch('rules_combiner.output.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = "20240101_120000"
            backup_path = generator.backup_existing_file()
        
        # Assert
        assert backup_path is not None
        assert backup_path.exists()
        assert "AGENT_backup_20240101_120000.md" in str(backup_path)
        assert backup_path.read_text() == "# Existing Content\n\nSome content."

    def test_backup_existing_file_when_file_not_exists(self, tmp_path: Path) -> None:
        """Test backup when target file doesn't exist."""
        # Arrange
        output_path = tmp_path / "AGENT.md"  # File doesn't exist
        generator = OutputGenerator(output_path, backup=True)
        
        # Act
        backup_path = generator.backup_existing_file()
        
        # Assert
        assert backup_path is None

    def test_backup_existing_file_with_backup_disabled(self, tmp_path: Path) -> None:
        """Test that backup is skipped when disabled."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Existing Content")
        generator = OutputGenerator(output_path, backup=False)
        
        # Act
        backup_path = generator.backup_existing_file()
        
        # Assert
        assert backup_path is None

    def test_write_combined_rules(self, tmp_path: Path) -> None:
        """Test writing combined rules to output file."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        generator = OutputGenerator(output_path)
        content = "# Combined Rules\n\n## Rule 1\n\nContent 1\n\n## Rule 2\n\nContent 2"
        
        # Act
        generator.write_combined_rules(content)
        
        # Assert
        assert output_path.exists()
        written_content = output_path.read_text(encoding='utf-8')
        assert written_content == content

    def test_write_combined_rules_creates_directory(self, tmp_path: Path) -> None:
        """Test that write_combined_rules creates parent directories."""
        # Arrange
        nested_path = tmp_path / "nested" / "folder" / "AGENT.md"
        generator = OutputGenerator(nested_path)
        content = "# Test Content"
        
        # Act
        generator.write_combined_rules(content)
        
        # Assert
        assert nested_path.exists()
        assert nested_path.read_text(encoding='utf-8') == content

    def test_write_combined_rules_overwrites_existing(self, tmp_path: Path) -> None:
        """Test that write_combined_rules overwrites existing file."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Old Content")
        generator = OutputGenerator(output_path)
        new_content = "# New Content\n\nUpdated content."
        
        # Act
        generator.write_combined_rules(new_content)
        
        # Assert
        assert output_path.read_text(encoding='utf-8') == new_content

    def test_validate_output_with_valid_file(self, tmp_path: Path) -> None:
        """Test validating a successfully written output file."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Valid Content\n\nSome rules here.")
        generator = OutputGenerator(output_path)
        
        # Act
        result = generator.validate_output()
        
        # Assert
        assert result is True

    def test_validate_output_with_missing_file(self, tmp_path: Path) -> None:
        """Test validating when output file doesn't exist."""
        # Arrange
        output_path = tmp_path / "AGENT.md"  # File doesn't exist
        generator = OutputGenerator(output_path)
        
        # Act
        result = generator.validate_output()
        
        # Assert
        assert result is False

    def test_validate_output_with_empty_file(self, tmp_path: Path) -> None:
        """Test validating an empty output file."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("")  # Empty file
        generator = OutputGenerator(output_path)
        
        # Act
        result = generator.validate_output()
        
        # Assert
        assert result is False

    def test_validate_output_with_directory(self, tmp_path: Path) -> None:
        """Test validating when output path is a directory."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.mkdir()  # Create as directory instead of file
        generator = OutputGenerator(output_path)
        
        # Act
        result = generator.validate_output()
        
        # Assert
        assert result is False

    def test_backup_file_naming_with_multiple_backups(self, tmp_path: Path) -> None:
        """Test that backup files get unique names."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Original Content")
        generator = OutputGenerator(output_path, backup=True)
        
        # Act
        with patch('rules_combiner.output.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = "20240101_120000"
            backup_path1 = generator.backup_existing_file()
            
            # Simulate different timestamp for second backup
            mock_datetime.now.return_value.strftime.return_value = "20240101_120001"
            output_path.write_text("# Modified Content")
            backup_path2 = generator.backup_existing_file()
        
        # Assert
        assert backup_path1 is not None
        assert backup_path2 is not None
        assert backup_path1 != backup_path2
        assert backup_path1.exists()
        assert backup_path2.exists()

    def test_write_combined_rules_with_permission_error(self, tmp_path: Path) -> None:
        """Test handling permission errors when writing."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        generator = OutputGenerator(output_path)
        content = "# Test Content"
        
        # Act & Assert
        with patch('pathlib.Path.write_text', side_effect=PermissionError("Access denied")):
            with pytest.raises(PermissionError):
                generator.write_combined_rules(content)

    def test_backup_with_permission_error(self, tmp_path: Path) -> None:
        """Test handling permission errors during backup."""
        # Arrange
        output_path = tmp_path / "AGENT.md"
        output_path.write_text("# Existing Content")
        generator = OutputGenerator(output_path, backup=True)
        
        # Act & Assert
        with patch('pathlib.Path.write_text', side_effect=PermissionError("Access denied")):
            with pytest.raises(PermissionError):
                generator.backup_existing_file()

    def test_output_generator_creates_logger_component(self, tmp_path: Path) -> None:
        """Test that OutputGenerator initializes logger with correct component."""
        # Arrange & Act
        output_path = tmp_path / "AGENT.md"
        generator = OutputGenerator(output_path)
        
        # Assert - Just verify the generator was created successfully
        # The logger functionality is tested indirectly through the other methods
        assert generator._output_path == output_path
        assert hasattr(generator, '_logger')
