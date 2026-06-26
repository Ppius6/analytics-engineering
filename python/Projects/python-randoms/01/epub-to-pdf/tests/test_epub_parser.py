"""Tests for epub_parser module."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from epub_parser import EpubParser


class TestEpubParser:
    """Tests for EpubParser class."""

    def test_init_sets_file_path(self):
        """Test that initialization sets the file path."""
        parser = EpubParser("/path/to/book.epub")

        assert parser.file_path == "/path/to/book.epub"
        assert parser.book is None
        assert parser.chapters == []

    def test_clean_html_extracts_text(self):
        """Test that HTML is cleaned and text is extracted."""
        parser = EpubParser("dummy.epub")
        html = "<html><body><p>Hello</p><p>World</p></body></html>"

        result = parser._clean_html(html)

        assert "Hello" in result
        assert "World" in result
        assert "<p>" not in result

    def test_clean_html_removes_tags(self):
        """Test that all HTML tags are removed."""
        parser = EpubParser("dummy.epub")
        html = "<div><strong>Bold</strong> and <em>italic</em></div>"

        result = parser._clean_html(html)

        assert "<div>" not in result
        assert "<strong>" not in result
        assert "Bold" in result
        assert "italic" in result
