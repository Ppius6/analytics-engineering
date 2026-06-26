"""Tests for pdf_generator module."""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_generator import PdfGenerator


class TestPdfGenerator:
    """Tests for PdfGenerator class."""

    def test_creates_pdf_file(self, tmp_path):
        """Test that a PDF file is created."""
        output_path = str(tmp_path / "output.pdf")
        generator = PdfGenerator(output_path)

        result = generator.create_from_text("Test Book", ["Chapter 1 content"])

        assert os.path.exists(result)
        assert result.endswith(".pdf")

    def test_pdf_with_multiple_chapters(self, tmp_path):
        """Test PDF creation with multiple chapters."""
        output_path = str(tmp_path / "multi_chapter.pdf")
        generator = PdfGenerator(output_path)
        chapters = [
            "This is chapter one.\n\nIt has multiple paragraphs.",
            "This is chapter two.\n\nAlso with paragraphs.",
        ]

        result = generator.create_from_text("Multi Chapter Book", chapters)

        assert os.path.exists(result)
        assert os.path.getsize(result) > 0

    def test_pdf_with_empty_chapters(self, tmp_path):
        """Test PDF creation with empty chapter list."""
        output_path = str(tmp_path / "empty.pdf")
        generator = PdfGenerator(output_path)

        result = generator.create_from_text("Empty Book", [])

        assert os.path.exists(result)

    def test_returns_output_path(self, tmp_path):
        """Test that create_from_text returns the output path."""
        output_path = str(tmp_path / "test.pdf")
        generator = PdfGenerator(output_path)

        result = generator.create_from_text("Title", ["Content"])

        assert result == output_path
