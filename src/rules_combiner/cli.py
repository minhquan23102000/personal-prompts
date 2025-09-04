"""Command-line interface for the Rules Combiner CLI."""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console

from .discovery import RuleDiscoveryEngine  
from .models import CombinationConfig
from .output import OutputGenerator
from .processor import RuleProcessor
from .selector import InteractiveSelector


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli() -> None:
    """Rules Combiner CLI - Combine rule files into a single AGENT.md file.
    
    This tool helps you select and combine multiple Markdown rule files from a
    rules directory into a single, well-formatted AGENT.md file with table of
    contents and proper section headers.
    """
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
    """Generate combined rules file interactively.
    
    Discovers rule files in the specified directory, presents them for
    interactive selection, and combines the selected rules into a single
    output file.
    """
    try:
        # Step 1: Discover rule files
        console.print(f"[cyan]Discovering rule files in: {rules_dir}[/cyan]")
        discovery_engine = RuleDiscoveryEngine(rules_dir)
        available_rules = discovery_engine.discover_rules()
        
        if not available_rules:
            console.print(f"[red]No rule files found in {rules_dir}[/red]")
            console.print("Please ensure the directory contains .md files.")
            sys.exit(1)
        
        console.print(f"[green]Found {len(available_rules)} rule files[/green]")
        
        # Step 2: Interactive selection
        console.print("\n[cyan]Select rules to combine:[/cyan]")
        selector = InteractiveSelector(available_rules)
        selected_filenames = selector.get_user_selection()
        
        if not selected_filenames:
            console.print("[yellow]No rules selected. Exiting.[/yellow]")
            sys.exit(0)
        
        # Filter selected rules
        selected_rules = [
            rule for rule in available_rules 
            if rule.filename in selected_filenames
        ]
        
        console.print(f"\n[green]Processing {len(selected_rules)} selected rules...[/green]")
        
        # Step 3: Process and combine rules
        processor = RuleProcessor()
        combined_content_parts = []
        
        # Generate table of contents if requested
        if not no_toc:
            toc = processor.generate_table_of_contents(selected_rules)
            combined_content_parts.append(toc)
        
        # Process each selected rule
        for rule in selected_rules:
            console.print(f"Processing: {rule.filename}")
            
            try:
                rule_content = processor.read_rule_content(rule.path)
                formatted_section = processor.format_rule_section(rule_content, rule.title)
                combined_content_parts.append(formatted_section)
                
            except Exception as e:
                console.print(f"[red]Error processing {rule.filename}: {e}[/red]")
                sys.exit(1)
        
        # Combine all parts
        combined_content = "\n".join(combined_content_parts)
        
        # Step 4: Generate output
        console.print(f"\n[cyan]Writing combined rules to: {output}[/cyan]")
        output_generator = OutputGenerator(output, backup=not no_backup)
        
        # Create backup if enabled and file exists
        if not no_backup:
            backup_path = output_generator.backup_existing_file()
            if backup_path:
                console.print(f"[yellow]Created backup: {backup_path}[/yellow]")
        
        # Write the combined content
        output_generator.write_combined_rules(combined_content)
        
        # Validate output
        if output_generator.validate_output():
            console.print(f"[green]✓ Successfully generated {output}[/green]")
            console.print(f"[dim]Combined {len(selected_rules)} rules into {output.stat().st_size:,} bytes[/dim]")
        else:
            console.print("[red]✗ Output file validation failed[/red]")
            sys.exit(1)
            
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)


@cli.command()
@click.option(
    "--rules-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default="rules"
)
def list_rules(rules_dir: Path) -> None:
    """List all available rule files.
    
    Shows all discoverable rule files in the specified directory with
    their titles and file sizes.
    """
    try:
        console.print(f"[cyan]Listing rule files in: {rules_dir}[/cyan]\n")
        
        discovery_engine = RuleDiscoveryEngine(rules_dir)
        available_rules = discovery_engine.discover_rules()
        
        if not available_rules:
            console.print(f"[red]No rule files found in {rules_dir}[/red]")
            return
        
        from rich.table import Table
        
        table = Table(title=f"Rule Files in {rules_dir}")
        table.add_column("Filename", style="magenta")
        table.add_column("Title", style="green")
        table.add_column("Size", justify="right", style="blue")
        table.add_column("~Tokens", justify="right", style="yellow")
        
        total_tokens = 0
        for rule in available_rules:
            file_size = f"{rule.file_size:,} bytes" if rule.file_size > 0 else "unknown"
            token_estimate = f"~{rule.estimated_tokens:,}" if rule.estimated_tokens > 0 else "~0"
            total_tokens += rule.estimated_tokens
            table.add_row(rule.filename, rule.title, file_size, token_estimate)
        
        console.print(table)
        console.print(f"\n[dim]Total: {len(available_rules)} rule files, ~{total_tokens:,} estimated tokens[/dim]")
        
    except Exception as e:
        console.print(f"[red]Error listing rules: {e}[/red]")
        sys.exit(1)


def main() -> None:
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
