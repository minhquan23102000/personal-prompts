"""Unit tests for RuleProcessor."""

import pytest
from pathlib import Path

from rules_combiner.processor import RuleProcessor
from rules_combiner.models import RuleFile


@pytest.fixture
def sample_rule_files(tmp_path: Path) -> list[RuleFile]:
    """Create sample rule files for testing."""
    files = []
    
    # Create rule file 1
    file1 = tmp_path / "rule1.md"
    file1.write_text("# Mental Model: Test Rule 1\n\nThis is the content of rule 1.\n\n## Details\n\nSome details here.")
    rule1 = RuleFile(file1, "rule1.md", "Mental Model: Test Rule 1")
    files.append(rule1)
    
    # Create rule file 2  
    file2 = tmp_path / "rule2.md"
    file2.write_text("# Test Rule 2\n\nThis is rule 2 content.\n\n### Subsection\n\nMore content.")
    rule2 = RuleFile(file2, "rule2.md", "Test Rule 2")
    files.append(rule2)
    
    return files


class TestRuleProcessor:
    """Test cases for RuleProcessor."""

    def test_rule_processor_initialization(self) -> None:
        """Test creating a RuleProcessor."""
        # Act
        processor = RuleProcessor()
        
        # Assert
        assert processor is not None

    def test_read_rule_content(self, sample_rule_files: list[RuleFile]) -> None:
        """Test reading content from a rule file."""
        # Arrange
        processor = RuleProcessor()
        rule = sample_rule_files[0]
        
        # Act
        content = processor.read_rule_content(rule.path)
        
        # Assert
        assert "Mental Model: Test Rule 1" in content
        assert "This is the content of rule 1." in content
        assert "## Details" in content

    def test_read_rule_content_with_nonexistent_file(self) -> None:
        """Test reading content from nonexistent file raises error."""
        # Arrange
        processor = RuleProcessor()
        nonexistent_path = Path("nonexistent.md")
        
        # Act & Assert
        with pytest.raises(FileNotFoundError):
            processor.read_rule_content(nonexistent_path)

    def test_format_rule_section(self) -> None:
        """Test formatting rule content as a section."""
        # Arrange
        processor = RuleProcessor()
        content = "# Original Title\n\nSome content here.\n\n## Subsection\n\nMore content."
        title = "Test Rule"
        
        # Act
        formatted = processor.format_rule_section(content, title)
        
        # Assert
        assert f"# {title}" in formatted
        assert "Some content here." in formatted
        assert "## Subsection" in formatted
        assert "More content." in formatted
        # Should not contain the original title as a header since it's replaced
        assert "# Original Title" not in formatted

    def test_format_rule_section_with_empty_content(self) -> None:
        """Test formatting empty content."""
        # Arrange  
        processor = RuleProcessor()
        content = ""
        title = "Empty Rule"
        
        # Act
        formatted = processor.format_rule_section(content, title)
        
        # Assert
        assert f"# {title}" in formatted
        assert len(formatted.strip()) > 0

    def test_format_rule_section_without_original_header(self) -> None:
        """Test formatting content that doesn't start with header."""
        # Arrange
        processor = RuleProcessor()
        content = "Just some content without header.\n\nMore content."
        title = "No Header Rule"
        
        # Act
        formatted = processor.format_rule_section(content, title)
        
        # Assert
        assert f"# {title}" in formatted
        assert "Just some content without header." in formatted

    def test_generate_table_of_contents(self, sample_rule_files: list[RuleFile]) -> None:
        """Test generating table of contents."""
        # Arrange
        processor = RuleProcessor()
        
        # Act
        toc = processor.generate_table_of_contents(sample_rule_files)
        
        # Assert
        assert "# Table of Contents" in toc
        assert "Mental Model: Test Rule 1" in toc
        assert "Test Rule 2" in toc
        # Should contain links/references to the rules
        assert len(toc.split("\n")) > 3  # Should be multiple lines

    def test_generate_table_of_contents_with_empty_list(self) -> None:
        """Test generating TOC with empty rule list."""
        # Arrange
        processor = RuleProcessor()
        
        # Act
        toc = processor.generate_table_of_contents([])
        
        # Assert
        assert "# Table of Contents" in toc
        assert "No rules selected" in toc or toc.strip() == "# Table of Contents"

    def test_generate_table_of_contents_with_long_titles(self, tmp_path: Path) -> None:
        """Test TOC generation with very long rule titles."""
        # Arrange
        processor = RuleProcessor()
        
        long_title = "This is a very long title that might need special handling in the table of contents"
        file1 = tmp_path / "long.md"
        file1.write_text(f"# {long_title}\n\nContent.")
        rule = RuleFile(file1, "long.md", long_title)
        
        # Act
        toc = processor.generate_table_of_contents([rule])
        
        # Assert
        assert "# Table of Contents" in toc
        assert long_title in toc

    def test_read_rule_content_with_encoding_issues(self, tmp_path: Path) -> None:
        """Test reading file with potential encoding issues."""
        # Arrange
        processor = RuleProcessor()
        
        # Create file with UTF-8 content including special characters
        file_path = tmp_path / "special.md"
        content = "# Special Characters: àáâãäå ñ 中文 🚀\n\nContent with émojis and ñoñ-ASCII."
        file_path.write_text(content, encoding='utf-8')
        
        # Act
        result = processor.read_rule_content(file_path)
        
        # Assert
        assert "Special Characters: àáâãäå" in result
        assert "中文 🚀" in result
        assert "émojis and ñoñ-ASCII" in result

    def test_remove_original_title_from_content(self) -> None:
        """Test that original title headers are removed from content."""
        # Arrange
        processor = RuleProcessor()
        content = "# Original Title\n\nSome content.\n\n## Subsection\n\nMore content."
        title = "New Title"
        
        # Act
        formatted = processor.format_rule_section(content, title)
        
        # Assert
        lines = formatted.split('\n')
        title_lines = [line for line in lines if line.strip().startswith('# ')]
        
        # Should only have one title line (the new one)
        assert len(title_lines) == 1
        assert title_lines[0].strip() == f"# {title}"

    def test_preserve_subsection_headers(self) -> None:
        """Test that subsection headers (##, ###) are preserved."""
        # Arrange
        processor = RuleProcessor()
        content = "# Original Title\n\n## Section 2\n\nContent.\n\n### Section 3\n\nMore."
        title = "New Title"
        
        # Act
        formatted = processor.format_rule_section(content, title)
        
        # Assert
        assert "## Section 2" in formatted
        assert "### Section 3" in formatted
