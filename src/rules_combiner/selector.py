"""Interactive selection interface for rule files."""

from typing import List

from rich.console import Console
from rich.table import Table

from .models import RuleFile


class InteractiveSelector:
    """Provides interactive selection interface for rules.
    
    This class creates a user-friendly interface for selecting multiple
    rule files using various input formats like individual numbers,
    ranges, and the 'all' keyword.
    
    Example:
        >>> rules = [RuleFile(...), RuleFile(...)]
        >>> selector = InteractiveSelector(rules)
        >>> selection = selector.get_user_selection()
        >>> print(f"Selected {len(selection)} rule files")
    """
    
    def __init__(self, available_rules: List[RuleFile]) -> None:
        """Initialize selector with available rule files.
        
        Args:
            available_rules: List of RuleFile objects available for selection.
        """
        self._rules = available_rules
        self._console = Console()
    
    def display_rules(self) -> None:
        """Display available rules in a formatted table.
        
        Shows a numbered list of available rule files with their titles,
        filenames, and file sizes in a nicely formatted table using Rich.
        """
        if not self._rules:
            self._console.print("[yellow]No rule files found.[/yellow]")
            return
        
        table = Table(title="Available Rule Files")
        table.add_column("No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("Filename", style="magenta")
        table.add_column("Title", style="green")
        table.add_column("Size", justify="right", style="blue")
        table.add_column("~Tokens", justify="right", style="yellow")
        
        for i, rule in enumerate(self._rules, 1):
            file_size = f"{rule.file_size:,} bytes" if rule.file_size > 0 else "unknown"
            token_estimate = f"~{rule.estimated_tokens:,}" if rule.estimated_tokens > 0 else "~0"
            table.add_row(str(i), rule.filename, rule.title, file_size, token_estimate)
        
        self._console.print(table)
        self._console.print()
    
    def get_user_selection(self) -> List[str]:
        """Get user selection through interactive prompts.
        
        Presents the available rules to the user and prompts for selection
        using various input formats. Continues prompting until the user
        confirms their selection.
        
        Returns:
            List of selected rule filenames.
            
        Example:
            User inputs "1,3-5" to select rules 1, 3, 4, and 5.
        """
        if not self._rules:
            self._console.print("[red]No rules available for selection.[/red]")
            return []
        
        while True:
            # Display available rules
            self.display_rules()
            
            # Show help text
            self._console.print("[bold cyan]Selection options:[/bold cyan]")
            self._console.print("• Individual numbers: [green]1,3,5[/green]")
            self._console.print("• Ranges: [green]1-3[/green] or [green]2-5[/green]")
            self._console.print("• Mixed: [green]1,3-5,7[/green]")
            self._console.print("• All: [green]all[/green]")
            self._console.print()
            
            # Get user input
            try:
                selection_input = input("Select rule files (e.g., 1,3-5 or 'all'): ").strip()
                
                if not selection_input:
                    self._console.print("[red]Please enter a selection.[/red]")
                    continue
                
                # Parse input and get selected indices
                selected_indices = self._parse_selection_input(selection_input)
                
                # Convert indices to filenames
                selected_filenames = [self._rules[i].filename for i in selected_indices]
                
                # Confirm selection
                if self.confirm_selection(selected_filenames):
                    return selected_filenames
                    
            except ValueError as e:
                self._console.print(f"[red]Invalid selection: {e}[/red]")
                self._console.print()
            except KeyboardInterrupt:
                self._console.print("\\n[yellow]Selection cancelled.[/yellow]")
                return []
    
    def confirm_selection(self, selected: List[str]) -> bool:
        """Confirm the user's selection before proceeding.
        
        Shows the selected rules and asks for confirmation.
        
        Args:
            selected: List of selected rule filenames.
            
        Returns:
            True if user confirms, False otherwise.
        """
        # Calculate total tokens for selected rules
        selected_rules = [rule for rule in self._rules if rule.filename in selected]
        total_tokens = sum(rule.estimated_tokens for rule in selected_rules)
        total_size = sum(rule.file_size for rule in selected_rules)
        
        self._console.print(f"\n[bold]Selected {len(selected)} rule files:[/bold]")
        for rule in selected_rules:
            self._console.print(f"  • {rule.filename} [dim](~{rule.estimated_tokens:,} tokens)[/dim]")
        
        self._console.print(f"\n[dim]Total: {total_size:,} bytes, ~{total_tokens:,} estimated tokens[/dim]")
        self._console.print()
        
        while True:
            try:
                confirm = input("Proceed with this selection? (y/n): ").lower().strip()
                if confirm in ['y', 'yes']:
                    return True
                elif confirm in ['n', 'no']:
                    return False
                else:
                    self._console.print("[red]Please enter 'y' for yes or 'n' for no.[/red]")
            except KeyboardInterrupt:
                return False
    
    def _parse_selection_input(self, selection_input: str) -> List[int]:
        """Parse user selection input into list of indices.
        
        Supports various input formats:
        - Individual numbers: "1,3,5"
        - Ranges: "1-3" 
        - Mixed: "1,3-5,7"
        - All: "all"
        
        Args:
            selection_input: User input string.
            
        Returns:
            List of 0-based indices for selected rules.
            
        Raises:
            ValueError: If input format is invalid or contains out-of-range numbers.
        """
        selection_input = selection_input.lower().strip()
        
        # Handle 'all' keyword
        if selection_input == "all":
            return list(range(len(self._rules)))
        
        indices = set()  # Use set to avoid duplicates
        
        # Split by comma to handle multiple parts
        parts = [part.strip() for part in selection_input.split(',')]
        
        for part in parts:
            if not part:
                continue
                
            if '-' in part:
                # Handle range (e.g., "1-3")
                try:
                    start_str, end_str = part.split('-', 1)
                    start = int(start_str.strip())
                    end = int(end_str.strip())
                    
                    if start < 1 or end < 1:
                        raise ValueError("Rule numbers must be 1 or greater")
                    if start > len(self._rules) or end > len(self._rules):
                        raise ValueError(f"Rule numbers must be between 1 and {len(self._rules)}")
                    if start > end:
                        raise ValueError("Invalid range: start must be <= end")
                    
                    # Convert to 0-based indices and add to set
                    for i in range(start - 1, end):
                        indices.add(i)
                        
                except ValueError as e:
                    if "invalid literal" in str(e):
                        raise ValueError(f"Invalid range format: '{part}'")
                    raise
            else:
                # Handle individual number
                try:
                    num = int(part)
                    if num < 1:
                        raise ValueError("Rule numbers must be 1 or greater")
                    if num > len(self._rules):
                        raise ValueError(f"Rule number {num} is out of range (max: {len(self._rules)})")
                    
                    # Convert to 0-based index
                    indices.add(num - 1)
                    
                except ValueError as e:
                    if "invalid literal" in str(e):
                        raise ValueError(f"Invalid number: '{part}'")
                    raise
        
        if not indices:
            raise ValueError("No valid rule numbers found in input")
        
        return sorted(list(indices))
