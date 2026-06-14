import pytest
from assistant.utils.system_platform import (
    is_windows, is_linux, is_mac, 
    detect_shell, get_os, get_system_info
)

def test_is_windows():
    result = is_windows()
    assert isinstance(result, bool)

def test_is_linux():
    result = is_linux()
    assert isinstance(result, bool)

def test_is_mac():
    result = is_mac()
    assert isinstance(result, bool)

def test_get_os():
    result = get_os()
    assert isinstance(result, str)
    assert result in ["Windows", "Linux", "Darwin"]

def test_detect_shell():
    result = detect_shell()
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_system_info():
    result = get_system_info()
    assert isinstance(result, dict)
    assert "os" in result
    assert "shell" in result
    assert "python_version" in result