import platform
import os

def is_windows():
    """Check if running on Windows"""
    return platform.system() == "Windows"

def is_linux():
    """Check if running on Linux"""
    return platform.system() == "Linux"

def is_mac():
    """Check if running on macOS"""
    return platform.system() == "Darwin"

def get_os():
    """Get operating system name"""
    return platform.system()

def detect_shell():
    """Detect the current shell being used"""
    # For Windows
    if is_windows():
        shell = os.environ.get("COMSPEC", "")
        if "powershell" in shell.lower():
            return "PowerShell"
        elif "cmd" in shell.lower():
            return "CMD"
        else:
            return "Unknown Windows Shell"
    
    # For Unix-like systems
    elif is_linux() or is_mac():
        shell = os.environ.get("SHELL", "")
        if "bash" in shell:
            return "Bash"
        elif "zsh" in shell:
            return "Zsh"
        elif "fish" in shell:
            return "Fish"
        else:
            return "Unknown Unix Shell"
    
    return "Unknown"

def get_os_version():
    """Get OS version information"""
    return platform.version()

def get_system_info():
    """Get complete system information"""
    return {
        "os": get_os(),
        "os_version": get_os_version(),
        "shell": detect_shell(),
        "python_version": platform.python_version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }
print(f'Is Windows: {is_windows()}'); 
print(f'Shell: {detect_shell()}'); 
print(f'System Info: {get_system_info()}')