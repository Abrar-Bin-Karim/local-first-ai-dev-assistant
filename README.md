<div align="center">

# Local First AI Dev Assistant

### A privacy-focused developer assistant for understanding repositories, logs, Git history, shell commands, and project context locally.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-00B4D8?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=for-the-badge)

</div>

---

## Overview

**Local First AI Dev Assistant** is a command-line developer tool designed to help engineers understand and inspect software projects while keeping workflows safe and local-first.

It focuses on repository exploration, Git reasoning, log analysis, shell command explanation, configuration management, and budget-aware assistant usage.

The project is read-only by default, making it useful for safely analyzing codebases without accidentally changing files.

---

## Key Features

- Repository structure explanation
- Directory tree visualization
- File discovery by pattern
- Repository statistics
- Git-related reasoning commands
- Log analysis utilities
- Shell command explanation
- Budget and usage control
- Configuration management
- Rich terminal output using `rich`
- CLI interface powered by `typer`

---

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.10+ |
| CLI Framework | Typer |
| Terminal UI | Rich |
| Config | PyYAML |
| Testing | Pytest |

---

## Project Structure

```text
local-first-ai-dev-assistant/
├── src/
│   └── assistant/
│       ├── cli.py
│       ├── commands/
│       │   ├── budget.py
│       │   ├── config.py
│       │   ├── git.py
│       │   ├── logs.py
│       │   ├── repo.py
│       │   └── shell.py
│       └── utils/
│           ├── config.py
│           ├── ignore.py
│           ├── system_platform.py
│           └── ui.py
├── tests/
├── pyproject.toml
├── LICENSE
└── README.md
Installation
Clone the repository:
git clone https://github.com/Abrar-Bin-Karim/local-first-ai-dev-assistant.git
cd local-first-ai-dev-assistant
Create and activate a virtual environment:
python -m venv .venv
On Windows:
.venv\Scripts\activate
On macOS/Linux:
source .venv/bin/activate
Install the package in editable mode:
pip install -e .
Usage
Check the installed version:
assistant version
Explain a repository:
assistant repo explain .
Display a directory tree:
assistant repo tree . --depth 3
List files by pattern:
assistant repo files "*.py"
Show repository statistics:
assistant repo stats
View available command groups:
assistant --help
Command Groups
Command Group
repo
git
logs
shell
budget
config
Testing
Install test dependencies if needed:
pip install pytest
Run tests:
pytest
Roadmap
- Add deeper repository summarization
- Improve Git history analysis
- Add more log parsers
- Add local model support
- Add safer command recommendation workflows
- Expand test coverage
License
This project is licensed under the MIT License.
<div align="center">
Built with Python, Typer, and Rich.
</div>
```
