---
name: uv-initialization
description:  This skill helps users initialize and set up Python projects using the uv package manager.
  It should be used when users need to create new Python projects, set up virtual environments,
  or manage dependencies with uv.
 
---

# UV Initialization Skill

## Overview
This skill provides comprehensive support for initializing and managing Python projects using the uv package manager. UV is an extremely fast Python package installer and resolver, written in Rust.

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Current project structure, existing Python setup, pyproject.toml or requirements.txt if present |
| **Conversation** | User's specific requirements for Python version, dependencies, project type |
| **Skill References** | UV commands, best practices, installation methods from `references/` |
| **User Guidelines** | Project-specific conventions, team standards for Python packaging |

Ensure all required context is gathered before implementing.
Only ask user for THEIR specific requirements (domain expertise is in this skill).

## Installation Methods

### Linux/macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Core Commands

### Project Initialization
```bash
uv init                    # Create a new project in current directory
uv init --python 3.12      # Create with specific Python version
uv init my-project         # Create project in named directory
```

### Dependency Management
```bash
uv add requests            # Add a dependency
uv add --dev pytest        # Add a development dependency
uv sync                    # Install all dependencies from pyproject.toml
uv remove package_name     # Remove a dependency
```

### Virtual Environment Management
```bash
uv venv                    # Create virtual environment
uv venv --seed             # Create with seed packages
uv run python script.py    # Run Python script in environment
uv run -m pytest          # Run Python module
```

### Python Version Management
```bash
uv python install 3.12     # Install specific Python version
uv python list            # List available Python versions
```

## Standard Workflow

### New Project Setup
1. Initialize the project:
   ```bash
   uv init my-project && cd my-project
   ```
2. Add dependencies:
   ```bash
   uv add fastapi pandas numpy
   ```
3. Sync and install:
   ```bash
   uv sync
   ```
4. Run your code:
   ```bash
   uv run python main.py
   ```

### Working with Existing Projects
1. Clone or navigate to the project
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run the project:
   ```bash
   uv run python main.py
   ```

## Advanced Features

### Lock File Management
```bash
uv lock                   # Generate/update uv.lock file
uv lock --locked          # Fail if lock file is out of date
```

### Publishing
```bash
uv build                  # Build distribution packages
uv publish                # Upload to PyPI
```

## Error Handling

Common issues and solutions:
- If `uv` command is not found: Ensure UV is installed and in PATH
- If Python version is not available: Use `uv python install <version>` to install it
- If dependencies conflict: Run `uv lock --upgrade` to resolve conflicts

## Best Practices

1. Always run `uv sync` after cloning a project
2. Use `uv run` to execute scripts in the proper environment
3. Pin critical dependencies to specific versions
4. Regularly update dependencies with `uv add --upgrade package_name`
5. Use virtual environments to isolate project dependencies