import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.assistant.utils.ui import (
    info, success, warning, error,
    confirm_prompt, text_prompt
)

# Rest of your test code...
import pytest
from src.assistant.utils.ui import (
    info, success, warning, error,
    confirm_prompt, text_prompt
)

def test_imports():
    """Test that all UI functions are importable"""
    from src.assistant.utils.ui import console, header, divider
    assert console is not None

def test_info_message(capsys):
    """Test info message display"""
    info("Test info")
    captured = capsys.readouterr()
    assert "Test info" in captured.out

def test_success_message(capsys):
    """Test success message display"""
    success("Test success")
    captured = capsys.readouterr()
    assert "Test success" in captured.out

def test_warning_message(capsys):
    """Test warning message display"""
    warning("Test warning")
    captured = capsys.readouterr()
    assert "Test warning" in captured.out

def test_error_message(capsys):
    """Test error message display"""
    error("Test error")
    captured = capsys.readouterr()
    assert "Test error" in captured.out