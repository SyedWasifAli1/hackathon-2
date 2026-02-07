# UV Package Manager - Comprehensive Reference

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Installation Details](#installation-details)
3. [Command Reference](#command-reference)
4. [Best Practices](#best-practices)
5. [Troubleshooting](#troubleshooting)
6. [Performance Benefits](#performance-benefits)
7. [Comparison with pip/pipenv](#comparison-with-pippipenv)

## Core Concepts

### What is UV?
UV is an extremely fast Python package installer and resolver, written in Rust. It serves as a drop-in replacement for pip and pip-tools, offering significant performance improvements for Python packaging operations.

### Key Features:
- Lightning-fast dependency resolution
- Drop-in replacement for pip
- Built-in virtual environment creation
- Fastest way to install Python packages
- Handles complex dependency graphs efficiently

### Architecture:
- Written in Rust for performance
- Compatible with PyPI and existing Python packaging standards
- Standalone binary with no dependencies
- Cross-platform support (Linux, macOS, Windows)

## Installation Details

### Linux/macOS Installation
```bash
# Install latest version
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or install to a specific directory
curl -LsSf https://astral.sh/uv/install.sh | sh -s -- -d ~/.local/bin
```

### Windows Installation
```powershell
# PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with specific destination
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" -Destination ~/.cargo/bin
```

### Manual Installation
Download the appropriate binary from GitHub releases:
- Linux: `uv-x86_64-unknown-linux-gnu.tar.gz`
- macOS: `uv-x86_64-apple-darwin.tar.gz` or `uv-aarch64-apple-darwin.tar.gz`
- Windows: `uv-x86_64-pc-windows-msvc.zip`

## Command Reference

### Project Management
```bash
uv init [OPTIONS] [PATH]
  --python TEXT              Target Python interpreter
  --name TEXT                Package name
  --no-readme               Do not create a README.md
  --no-pin-python           Do not pin the Python version in pyproject.toml
  --virtual-env             Create a virtual environment
```

### Dependency Management
```bash
uv add [OPTIONS] [PACKAGES]...
  --dev                     Add as development dependency
  --optional TEXT           Add to optional dependency group
  --group TEXT              Add to dependency group
  --editable                Add as editable
  --index-url URL           Index URL for package discovery

uv remove [OPTIONS] [PACKAGES]...
  --dev                     Remove from development dependencies

uv sync [OPTIONS]
  --locked                  Assert that the lockfile is up-to-date
  --frozen                  Don't update the lockfile
  --all-extras              Include all optional dependencies
  --extra TEXT              Include specific optional dependencies
```

### Virtual Environment Management
```bash
uv venv [OPTIONS] [PATH]
  --seed                    Include seed packages (pip, setuptools)
  --python TEXT            Target Python interpreter
  --prompt TEXT            Custom prompt for the virtual environment

uv run [OPTIONS] COMMAND [ARGS]...
  --with PACKAGES...        Run with additional packages installed
  --with-requirements FILE Install packages from requirements file
  --isolated               Run in an isolated virtual environment
```

### Python Management
```bash
uv python list              # List available Python versions
uv python install [VERSION] # Install specific Python version
uv python uninstall VERSION # Uninstall Python version
uv python find VERSION      # Find a Python interpreter
```

### Advanced Commands
```bash
uv lock [OPTIONS]           # Update the lockfile
  --upgrade-package TEXT    Upgrade specific packages
  --upgrade-all             Upgrade all packages

uv build [OPTIONS]          # Build distributions
  --sdist                   Build source distribution
  --wheel                   Build wheel
  --all-targets            Build all targets

uv publish [OPTIONS]        # Publish to registries
  --repository-url URL      Repository URL
  --username TEXT           Username
  --password TEXT           Password
```

## Best Practices

### 1. Project Setup Workflow
```
1. uv init my-project
2. cd my-project
3. uv add requests flask  # Add dependencies
4. uv sync               # Install everything
5. uv run python app.py  # Run in environment
```

### 2. Dependency Management
- Pin critical dependencies to prevent breaking changes
- Use `uv add --dev pytest black flake8` for development tools
- Regularly update with `uv sync --upgrade`
- Leverage dependency groups for different environments

### 3. Virtual Environment Usage
- Use `uv venv` to create isolated environments
- Activate with `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\Activate.ps1` (Windows)
- Keep project dependencies separate from global Python installation

### 4. Lock Files
- Commit `uv.lock` to version control
- Use `uv sync --locked` in CI/CD to ensure reproducible builds
- Run `uv lock` when dependencies change

### 5. Python Version Management
- Specify Python version in `pyproject.toml` or use `--python` flag
- Use `uv python install` to install specific Python versions
- Check compatibility before upgrading Python versions

## Troubleshooting

### Common Issues and Solutions

#### Issue: Command not found
**Solution:** Ensure UV is in PATH
```bash
# Add to shell profile
export PATH="$HOME/.cargo/bin:$PATH"  # Adjust path as needed
```

#### Issue: Dependency conflicts
**Solution:** Update lock file
```bash
uv lock --upgrade
uv sync
```

#### Issue: Python version not found
**Solution:** Install required Python version
```bash
uv python install 3.11
uv venv --python 3.11
```

#### Issue: Permission errors
**Solution:** Use appropriate permissions or install locally
```bash
# Install to user directory
uv venv --seed --python 3.11
```

#### Issue: Network connectivity problems
**Solution:** Configure proxy or index URL
```bash
uv pip install --index-url https://pypi.org/simple/ package_name
```

### Debugging Commands
```bash
uv --verbose                # Show detailed output
uv cache clean             # Clear UV cache
uv cache dir               # Show cache directory
```

## Performance Benefits

### Speed Comparison (vs pip)
- Dependency resolution: Up to 100x faster
- Installation: 5-10x faster
- Virtual environment creation: 2-3x faster
- Overall project setup: 5-15x faster

### Memory Efficiency
- Lower memory usage during resolution
- Faster startup times
- Reduced I/O operations

### Concurrency
- Parallel dependency downloads
- Concurrent installations
- Optimized network requests

## Comparison with pip/pipenv

### UV vs pip
| Feature | pip | UV |
|---------|-----|-----|
| Speed | Slow | Very Fast |
| Resolution | Python-based | Rust-based |
| Dependencies | Many | Standalone |
| Virtual Environments | Separate tools | Built-in |
| Lock files | None native | Built-in |

### UV vs pipenv
| Feature | pipenv | UV |
|---------|--------|-----|
| Speed | Moderate | Very Fast |
| Complexity | Higher | Lower |
| Virtual Envs | Built-in | Built-in |
| Lock files | Pipfile.lock | uv.lock |
| Python mgmt | Limited | Extensive |

### When to Use UV
- New Python projects (recommended)
- Performance-critical environments
- CI/CD pipelines
- Large dependency trees
- Teams wanting simplified workflows

### When to Stick with pip
- Legacy systems with strict tooling requirements
- Environments with complex pip-specific configurations
- When using tools that specifically require pip