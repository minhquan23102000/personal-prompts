"""End-to-end integration tests for the Rules Combiner CLI."""

import pytest
from pathlib import Path
from unittest.mock import patch

from rules_combiner.cli import generate
from rules_combiner.discovery import RuleDiscoveryEngine
from rules_combiner.processor import RuleProcessor
from rules_combiner.output import OutputGenerator


class TestEndToEndIntegration:
    """Integration tests for complete workflow."""
    
    def test_complete_workflow_with_sample_rules(self, tmp_path: Path) -> None:
        """Test the complete workflow from discovery to output generation."""
        # Arrange - Create sample rule files
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        # Rule 1
        rule1 = rules_dir / "rule1.md"
        rule1.write_text("""# Mental Model: Test Rule 1

This is the first test rule.

## Core Principles

- Principle 1
- Principle 2

## Best Practices

- Practice 1
- Practice 2
""")
        
        # Rule 2
        rule2 = rules_dir / "rule2.md"
        rule2.write_text("""# Mental Model: Test Rule 2

This is the second test rule.

## Guidelines

- Guideline 1
- Guideline 2
""")
        
        output_file = tmp_path / "AGENT.md"
        
        # Act - Simulate the complete workflow
        # Step 1: Discovery
        discovery = RuleDiscoveryEngine(rules_dir)
        available_rules = discovery.discover_rules()
        
        # Step 2: Process rules (simulate selecting all)
        processor = RuleProcessor()
        
        # Generate TOC
        toc = processor.generate_table_of_contents(available_rules)
        
        # Process each rule
        combined_parts = [toc]
        for rule in available_rules:
            content = processor.read_rule_content(rule.path)
            formatted = processor.format_rule_section(content, rule.title)
            combined_parts.append(formatted)
        
        combined_content = "\n".join(combined_parts)
        
        # Step 3: Generate output
        output_generator = OutputGenerator(output_file)
        output_generator.write_combined_rules(combined_content)
        
        # Assert
        assert output_file.exists()
        assert output_generator.validate_output()
        
        # Verify content structure
        content = output_file.read_text()
        assert "# Table of Contents" in content
        assert "Mental Model: Test Rule 1" in content
        assert "Mental Model: Test Rule 2" in content
        assert "## Core Principles" in content
        assert "## Guidelines" in content
        assert len(available_rules) == 2

    def test_backup_functionality(self, tmp_path: Path) -> None:
        """Test that backup functionality works correctly."""
        # Arrange
        output_file = tmp_path / "AGENT.md"
        output_file.write_text("# Existing Content\n\nThis is existing content.")
        
        # Act
        generator = OutputGenerator(output_file, backup=True)
        backup_path = generator.backup_existing_file()
        
        # Write new content
        new_content = "# New Content\n\nThis is new content."
        generator.write_combined_rules(new_content)
        
        # Assert
        assert backup_path is not None
        assert backup_path.exists()
        assert "backup" in backup_path.name
        assert backup_path.read_text() == "# Existing Content\n\nThis is existing content."
        assert output_file.read_text() == new_content

    def test_handling_of_nonexistent_rules_dir(self, tmp_path: Path) -> None:
        """Test handling when rules directory doesn't exist."""
        # Arrange
        nonexistent_dir = tmp_path / "nonexistent"
        
        # Act
        discovery = RuleDiscoveryEngine(nonexistent_dir)
        rules = discovery.discover_rules()
        
        # Assert - Should return empty list, not crash
        assert rules == []

    def test_table_of_contents_generation(self, tmp_path: Path) -> None:
        """Test that table of contents is generated correctly."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        rule1 = rules_dir / "first.md"
        rule1.write_text("# First Rule\n\nContent 1")
        
        rule2 = rules_dir / "second.md"
        rule2.write_text("# Second Rule\n\nContent 2")
        
        # Act
        discovery = RuleDiscoveryEngine(rules_dir)
        rules = discovery.discover_rules()
        
        processor = RuleProcessor()
        toc = processor.generate_table_of_contents(rules)
        
        # Assert
        assert "# Table of Contents" in toc
        assert "First Rule" in toc
        assert "Second Rule" in toc
        assert "[First Rule](#first-rule)" in toc or "[First Rule]" in toc
        assert "[Second Rule](#second-rule)" in toc or "[Second Rule]" in toc

    def test_rule_formatting_preserves_structure(self, tmp_path: Path) -> None:
        """Test that rule formatting preserves the original structure."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        rule_file = rules_dir / "complex.md"
        original_content = """# Original Title

This is the introduction.

## Section 1

Content for section 1.

### Subsection 1.1

Detailed content.

## Section 2

Content for section 2.

- List item 1
- List item 2

### Subsection 2.1

More content.
"""
        rule_file.write_text(original_content)
        
        # Act
        processor = RuleProcessor()
        content = processor.read_rule_content(rule_file)
        formatted = processor.format_rule_section(content, "New Title")
        
        # Assert
        assert "# New Title" in formatted
        assert "# Original Title" not in formatted  # Original title should be replaced
        assert "## Section 1" in formatted  # Subsections preserved
        assert "### Subsection 1.1" in formatted
        assert "### Subsection 2.1" in formatted
        assert "- List item 1" in formatted  # Lists preserved
        assert "- List item 2" in formatted

    def test_output_validation(self, tmp_path: Path) -> None:
        """Test output validation with various scenarios."""
        # Test valid file
        valid_file = tmp_path / "valid.md"
        valid_file.write_text("# Valid Content\n\nSome content here.")
        
        generator = OutputGenerator(valid_file)
        assert generator.validate_output() is True
        
        # Test empty file
        empty_file = tmp_path / "empty.md"
        empty_file.write_text("")
        
        empty_generator = OutputGenerator(empty_file)
        assert empty_generator.validate_output() is False
        
        # Test non-existent file
        missing_file = tmp_path / "missing.md"
        missing_generator = OutputGenerator(missing_file)
        assert missing_generator.validate_output() is False

    def test_unicode_handling(self, tmp_path: Path) -> None:
        """Test that the system handles Unicode characters correctly."""
        # Arrange
        rules_dir = tmp_path / "rules"
        rules_dir.mkdir()
        
        unicode_rule = rules_dir / "unicode.md"
        unicode_content = """# Mental Model: Unicode Test 🚀

This rule contains various Unicode characters:

## International Characters

- Français: café, naïve, résumé
- Español: niño, corazón, mañana
- 中文: 你好世界
- العربية: مرحبا بالعالم
- Русский: Привет мир

## Emojis and Symbols

- 🔥 Fire
- ⚡ Lightning
- 💡 Idea
- ✅ Check mark
- ❌ Cross mark

## Math Symbols

- α, β, γ, δ, ε
- ∑, ∏, ∫, ∂, ∇
- ≤, ≥, ≠, ≈, ∞
"""
        unicode_rule.write_text(unicode_content, encoding='utf-8')
        
        output_file = tmp_path / "unicode_output.md"
        
        # Act
        discovery = RuleDiscoveryEngine(rules_dir)
        rules = discovery.discover_rules()
        
        processor = RuleProcessor()
        content = processor.read_rule_content(rules[0].path)
        formatted = processor.format_rule_section(content, rules[0].title)
        
        generator = OutputGenerator(output_file)
        generator.write_combined_rules(formatted)
        
        # Assert
        assert output_file.exists()
        result_content = output_file.read_text(encoding='utf-8')
        
        # Check that Unicode characters are preserved
        assert "🚀" in result_content
        assert "café" in result_content
        assert "你好世界" in result_content
        assert "مرحبا بالعالم" in result_content
        assert "Привет мир" in result_content
        assert "∑" in result_content
        assert "≠" in result_content
