"""Markdown Link Checker."""

from .core import check_markdown_file, check_markdown_string
from .cli import main

__version__ = "0.1.0"
__author__ = "Bruce Studios"
__all__ = ["check_markdown_file", "check_markdown_string", "main"]