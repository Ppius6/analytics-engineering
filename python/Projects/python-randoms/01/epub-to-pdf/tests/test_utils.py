"""Tests for utils module."""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import validate_file, generate_output_path


class TestValidateFile:
    """Tests for validate_file function."""

    def test_file_not_found_raises_error(self):
        """Test that FileNotFoundError is raised for missing file."""
        with pytest.raises(FileNotFoundError):
            validate_file("nonexistent_file.epub")

    def test_wrong_extension_raises_error(self, tmp_path):
        """Test that ValueError is raised for wrong extension."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")

        with pytest.raises(ValueError, match="must have .epub extension"):
            validate_file(str(test_file), extension=".epub")

    def test_valid_file_returns_true(self, tmp_path):
        """Test that valid file returns True."""
        test_file = tmp_path / "test.epub"
        test_file.write_text("test content")

        assert validate_file(str(test_file), extension=".epub") is True

    def test_valid_file_no_extension_check(self, tmp_path):
        """Test validation without extension requirement."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test")

        assert validate_file(str(test_file)) is True


class TestGenerateOutputPath:
    """Tests for generate_output_path function."""

    def test_replaces_epub_with_pdf(self):
        """Test that .epub is replaced with .pdf."""
        result = generate_output_path("/path/to/book.epub")
        assert result == "/path/to/book.pdf"

    def test_preserves_directory(self):
        """Test that directory path is preserved."""
        result = generate_output_path("/home/user/documents/mybook.epub")
        assert result == "/home/user/documents/mybook.pdf"

    def test_custom_output_directory(self, tmp_path):
        """Test output to custom directory."""
        output_dir = str(tmp_path / "output")
        result = generate_output_path("book.epub", output_dir)

        assert result == os.path.join(output_dir, "book.pdf")
        assert os.path.exists(output_dir)  # Directory should be created
