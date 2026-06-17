<div align="center">

# 🚀 Local First AI Dev Assistant

### Privacy-First • Repository Intelligence • Developer Productivity

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&center=true&vCenter=true&width=900&lines=Understand+Repositories+Faster;Analyze+Logs+and+Git+History;Explain+Shell+Commands;Privacy-Focused+Local+Workflows;Built+for+Developers" />

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-00B4D8?style=for-the-badge)
![Typer](https://img.shields.io/badge/Typer-CLI_Framework-green?style=for-the-badge)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=for-the-badge)

</div>

---

## 📖 Overview

**Local First AI Dev Assistant** is a developer-focused command-line tool designed to help engineers understand, inspect, and navigate software projects while keeping workflows safe, transparent, and local-first.

Unlike cloud-dependent coding assistants, this project prioritizes:

✅ Privacy

✅ Local execution

✅ Read-only analysis

✅ Repository understanding

✅ Developer productivity

The assistant helps developers explore repositories, inspect logs, analyze Git history, understand shell commands, and manage project context without modifying source code.

---

## 🎯 Why This Project?

Modern codebases can become difficult to understand, especially when joining new projects or maintaining legacy systems.

This tool aims to answer questions like:

* What does this repository do?
* How is the project structured?
* Which files are important?
* What happened in recent Git history?
* What does this shell command actually do?
* What are these logs trying to tell me?

All while keeping analysis local and under the developer's control.

---

## ✨ Features

### 📂 Repository Intelligence

* Repository explanation
* Directory tree visualization
* Repository statistics
* File discovery by pattern
* Project structure analysis

### 🌳 Git Analysis

* Git history inspection
* Commit reasoning
* Repository activity understanding

### 📜 Log Exploration

* Log inspection utilities
* Pattern discovery
* Troubleshooting assistance

### 💻 Shell Command Understanding

* Command explanation
* Syntax breakdown
* Safety awareness

### ⚙️ Configuration & Budget Control

* YAML configuration management
* Usage monitoring
* Budget-aware workflows

### 🎨 Rich Terminal Experience

* Colorized output
* Better readability
* Enhanced developer experience

---

## 🏗️ Architecture

```text
local-first-ai-dev-assistant/
│
├── src/
│   └── assistant/
│       ├── cli.py
│       │
│       ├── commands/
│       │   ├── repo.py
│       │   ├── git.py
│       │   ├── logs.py
│       │   ├── shell.py
│       │   ├── budget.py
│       │   └── config.py
│       │
│       └── utils/
│           ├── config.py
│           ├── ignore.py
│           ├── system_platform.py
│           └── ui.py
│
├── tests/
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## 🛠️ Technology Stack

| Component     | Technology   |
| ------------- | ------------ |
| Language      | Python 3.10+ |
| CLI Framework | Typer        |
| Terminal UI   | Rich         |
| Configuration | PyYAML       |
| Testing       | Pytest       |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Abrar-Bin-Karim/local-first-ai-dev-assistant.git
cd local-first-ai-dev-assistant
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install the Project

```bash
pip install -e .
```

---

## 📚 Usage Examples

### Show Installed Version

```bash
assistant version
```

### Explain a Repository

```bash
assistant repo explain .
```

### Visualize Project Structure

```bash
assistant repo tree . --depth 3
```

### Find Files by Pattern

```bash
assistant repo files "*.py"
```

### Repository Statistics

```bash
assistant repo stats
```

### View All Available Commands

```bash
assistant --help
```

---

## 🧩 Command Groups

| Group  | Description                         |
| ------ | ----------------------------------- |
| repo   | Repository exploration and analysis |
| git    | Git history inspection              |
| logs   | Log analysis tools                  |
| shell  | Shell command explanation           |
| budget | Usage tracking and limits           |
| config | Configuration management            |

---

## 🧪 Running Tests

Install testing dependencies:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest
```

---

## 🛣️ Roadmap

### Near Term

* [ ] Enhanced repository summarization
* [ ] Better Git history reasoning
* [ ] Advanced log parsing
* [ ] Expanded test coverage

### Future Goals

* [ ] Local LLM integration
* [ ] Repository knowledge indexing
* [ ] Intelligent developer workflows
* [ ] Context-aware project analysis
* [ ] Plugin architecture

---

## 🤝 Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

<div align="center">

### 💡 Built for developers who value privacy, transparency, and understanding.

⭐ If you find this project useful, consider giving it a star.

</div>
