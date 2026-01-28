# Quick Reference for uv

## What is uv?

- Fast Python package installer and resolver written in Rust
- Modern replacement for `pip`, `venv`, and `virtualenv`
- Significantly faster and more reliable dependency resolution
- Backward compatible with `pip`

## Creating Virtual Environments

```bash
uv venv env                    # Create a virtual environment
uv venv env --python 3.11      # Specify Python version
```

## Activation

```bash
source env/bin/activate        # macOS/Linux
env\Scripts\activate           # Windows
```

## Project-Based Workflow with pyproject.toml

```bash
uv add django                  # Add dependency to pyproject.toml
uv add requests pandas         # Add multiple packages
uv sync                        # Sync environment with pyproject.toml
uv remove package-name         # Remove a dependency
```

The key differences are:

- `uv venv` - Creates virtual environment (replaces `python -m venv`)
- `uv pip install` - Installs in active venv (replaces `pip install`)
- `uv add` - Manages dependencies in `pyproject.toml` (modern workflow)
- Virtual environments created by `uv` are stored in `.venv` by default
- Activation works the same as standard Python virtual environments

## Note

- When using `uv add`, it automatically manages a `.venv` directory
- You still need to activate the virtual environment before using `django-admin` or other installed commands
- The `(python)` or (`.venv`) prefix in your terminal indicates the environment is active.
