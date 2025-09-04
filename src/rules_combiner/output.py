"""Output generator for creating the final combined rules file."""

from datetime import datetime
from pathlib import Path
from typing import Optional

from loguru import logger


class OutputGenerator:
    """Generates the final combined rules file.
    
    This class handles writing the combined rules content to the output file,
    creating backups of existing files, and validating the output.
    
    Example:
        >>> generator = OutputGenerator(Path("AGENT.md"))
        >>> generator.write_combined_rules(combined_content)
        >>> generator.validate_output()
        True
    """
    
    def __init__(self, output_path: Path, backup: bool = True) -> None:
        """Initialize generator with output path and backup preference.
        
        Args:
            output_path: Path where the combined rules file will be written.
            backup: Whether to create backups of existing files.
        """
        self._output_path = output_path
        self._backup_enabled = backup
        self._logger = logger.bind(component="output")
    
    def backup_existing_file(self) -> Optional[Path]:
        """Create a backup of the existing output file if it exists.
        
        Creates a backup file with a timestamp suffix in the same directory
        as the output file. Only creates a backup if backup is enabled and
        the target file exists.
        
        Returns:
            Path to the backup file if created, None otherwise.
            
        Raises:
            PermissionError: If there are permission issues creating the backup.
        """
        if not self._backup_enabled:
            self._logger.debug("Backup disabled, skipping backup creation")
            return None
        
        if not self._output_path.exists():
            self._logger.debug(f"Output file {self._output_path} does not exist, no backup needed")
            return None
        
        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{self._output_path.stem}_backup_{timestamp}{self._output_path.suffix}"
        backup_path = self._output_path.parent / backup_filename
        
        try:
            # Read existing content and write to backup
            existing_content = self._output_path.read_text(encoding='utf-8')
            backup_path.write_text(existing_content, encoding='utf-8')
            
            self._logger.info(f"Created backup file: {backup_path}")
            return backup_path
            
        except (OSError, PermissionError) as e:
            self._logger.error(f"Failed to create backup file {backup_path}: {e}")
            raise
    
    def write_combined_rules(self, content: str) -> None:
        """Write the combined rules content to the output file.
        
        Creates parent directories if they don't exist and writes the content
        to the output file using UTF-8 encoding.
        
        Args:
            content: The combined rules content to write.
            
        Raises:
            PermissionError: If there are permission issues writing the file.
            OSError: If there are other I/O issues.
        """
        try:
            # Create parent directories if they don't exist
            self._output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write the content to the file
            self._output_path.write_text(content, encoding='utf-8')
            
            self._logger.info(f"Successfully wrote combined rules to: {self._output_path}")
            self._logger.debug(f"Output file size: {self._output_path.stat().st_size} bytes")
            
        except (OSError, PermissionError) as e:
            self._logger.error(f"Failed to write output file {self._output_path}: {e}")
            raise
    
    def validate_output(self) -> bool:
        """Validate that the output file was written correctly.
        
        Checks that the output file exists, is a regular file, and contains
        some content.
        
        Returns:
            True if the output file is valid, False otherwise.
        """
        try:
            if not self._output_path.exists():
                self._logger.warning(f"Output file does not exist: {self._output_path}")
                return False
            
            if not self._output_path.is_file():
                self._logger.warning(f"Output path is not a file: {self._output_path}")
                return False
            
            # Check that the file has some content
            file_size = self._output_path.stat().st_size
            if file_size == 0:
                self._logger.warning(f"Output file is empty: {self._output_path}")
                return False
            
            # Try to read the file to ensure it's readable
            try:
                content = self._output_path.read_text(encoding='utf-8')
                if not content.strip():
                    self._logger.warning(f"Output file contains only whitespace: {self._output_path}")
                    return False
            except UnicodeDecodeError as e:
                self._logger.warning(f"Output file has encoding issues: {self._output_path}, {e}")
                return False
            
            self._logger.info(f"Output file validation successful: {self._output_path}")
            self._logger.debug(f"Validated file size: {file_size} bytes, content length: {len(content)} chars")
            return True
            
        except (OSError, PermissionError) as e:
            self._logger.error(f"Error validating output file {self._output_path}: {e}")
            return False
