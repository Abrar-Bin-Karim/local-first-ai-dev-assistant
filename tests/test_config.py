import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import yaml
from assistant.utils.config import (
    load_config, 
    create_default_config, 
    save_config,
    get_config_value,
    set_config_value,
    CONFIG_PATH
)

def test_config_path():
    """Test config path is in home directory"""
    assert str(CONFIG_PATH).endswith(".assistant.yaml")

def test_load_config_empty():
    """Test loading config when file doesn't exist"""
    original_exists = CONFIG_PATH.exists()
    if original_exists:
        with open(CONFIG_PATH, 'r') as f:
            backup = f.read()
        CONFIG_PATH.unlink()
    
    config = load_config()
    assert isinstance(config, dict)
    
    if original_exists:
        with open(CONFIG_PATH, 'w') as f:
            f.write(backup)

def test_create_default_config():
    """Test creating default configuration"""
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()
    
    config = create_default_config()
    assert isinstance(config, dict)
    assert "budget_limit" in config
    assert "theme" in config
    assert "shell" in config
    assert config["budget_limit"] == 10
    assert config["theme"] == "dark"
    
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()

def test_get_config_value():
    """Test getting specific config values"""
    create_default_config()
    
    assert get_config_value("budget_limit") == 10
    assert get_config_value("theme") == "dark"
    assert get_config_value("nonexistent", "default") == "default"
    
    CONFIG_PATH.unlink()

def test_set_config_value():
    """Test setting specific config values"""
    create_default_config()
    
    set_config_value("budget_limit", 20)
    set_config_value("new_key", "new_value")
    
    config = load_config()
    assert config["budget_limit"] == 20
    assert config["new_key"] == "new_value"
    
    CONFIG_PATH.unlink()