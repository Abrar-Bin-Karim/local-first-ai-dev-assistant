import pytest
from assistant.utils.ui import show_info, show_success, show_warning, show_error, show_header, show_table

def test_show_info(capsys):
    show_info("test message")
    captured = capsys.readouterr()
    assert "test message" in captured.out

def test_show_success(capsys):
    show_success("done")
    captured = capsys.readouterr()
    assert "done" in captured.out

def test_show_warning(capsys):
    show_warning("careful")
    captured = capsys.readouterr()
    assert "careful" in captured.out

def test_show_error(capsys):
    show_error("fail")
    captured = capsys.readouterr()
    assert "fail" in captured.out

def test_show_header(capsys):
    show_header("Header")
    captured = capsys.readouterr()
    assert "Header" in captured.out