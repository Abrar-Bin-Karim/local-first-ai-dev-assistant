from pathlib import Path
import yaml

CONFIG_PATH = Path.home() / ".assistant.yaml"

def load_config():
    """Load configuration from ~/.assistant.yaml"""
    if not CONFIG_PATH.exists():
        return {}

    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f) or {}

def create_default_config():
    """Create a default configuration file"""
    config = {
        "budget_limit": 10,
        "theme": "dark",
        "shell": "powershell"
    }

    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    
    return config

def save_config(config):
    """Save configuration to ~/.assistant.yaml"""
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False)

def get_config_value(key, default=None):
    """Get a specific configuration value"""
    config = load_config()
    return config.get(key, default)

def set_config_value(key, value):
    """Set a specific configuration value"""
    config = load_config()
    config[key] = value
    save_config(config)