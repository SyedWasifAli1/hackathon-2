#!/bin/bash
# uv-initialization-script.sh
# Script to help initialize Python projects with UV

set -e  # Exit on any error

show_help() {
    echo "UV Project Initialization Script"
    echo ""
    echo "Usage: $0 [OPTIONS] [PROJECT_NAME]"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -p, --python VERSION    Specify Python version (e.g., 3.11, 3.12)"
    echo "  -d, --deps DEPS         Comma-separated list of dependencies to add"
    echo "  --dev-deps DEPS         Comma-separated list of dev dependencies"
    echo "  --no-vcs               Skip git initialization"
    echo "  --no-readme            Skip README creation"
    echo ""
    echo "Examples:"
    echo "  $0 my-project                    # Create project with default settings"
    echo "  $0 -p 3.12 my-api              # Create project with Python 3.12"
    echo "  $0 -d 'requests,flask' my-web  # Create with dependencies"
}

# Default values
PYTHON_VERSION=""
DEPENDENCIES=""
DEV_DEPENDENCIES=""
INIT_VCS=1
INIT_README=1
PROJECT_NAME=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -p|--python)
            PYTHON_VERSION="$2"
            shift 2
            ;;
        -d|--deps)
            DEPENDENCIES="$2"
            shift 2
            ;;
        --dev-deps)
            DEV_DEPENDENCIES="$2"
            shift 2
            ;;
        --no-vcs)
            INIT_VCS=0
            shift
            ;;
        --no-readme)
            INIT_README=0
            shift
            ;;
        -*)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
        *)
            PROJECT_NAME="$1"
            shift
            ;;
    esac
done

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "Error: UV is not installed. Please install UV first."
    echo "Visit: https://github.com/astral-sh/uv"
    exit 1
fi

# If no project name provided, use current directory
if [ -z "$PROJECT_NAME" ]; then
    PROJECT_NAME=$(basename "$(pwd)")
    echo "Using current directory name: $PROJECT_NAME"
else
    # Create project directory if it doesn't exist
    if [ ! -d "$PROJECT_NAME" ]; then
        mkdir -p "$PROJECT_NAME"
    fi
    cd "$PROJECT_NAME" || exit
fi

echo "Initializing Python project: $PROJECT_NAME"

# Initialize the project with UV
INIT_CMD="uv init"
if [ -n "$PYTHON_VERSION" ]; then
    INIT_CMD="$INIT_CMD --python $PYTHON_VERSION"
fi

if [ $INIT_VCS -eq 0 ]; then
    INIT_CMD="$INIT_CMD --no-git"
fi

if [ $INIT_README -eq 0 ]; then
    INIT_CMD="$INIT_CMD --no-readme"
fi

eval $INIT_CMD

echo "Project initialized successfully!"

# Add dependencies if provided
if [ -n "$DEPENDENCIES" ]; then
    echo "Adding dependencies: $DEPENDENCIES"
    IFS=',' read -ra DEPS_ARRAY <<< "$DEPENDENCIES"
    for dep in "${DEPS_ARRAY[@]}"; do
        dep=$(echo $dep | xargs)  # Trim whitespace
        if [ -n "$dep" ]; then
            uv add "$dep"
        fi
    done
fi

# Add dev dependencies if provided
if [ -n "$DEV_DEPENDENCIES" ]; then
    echo "Adding dev dependencies: $DEV_DEPENDENCIES"
    IFS=',' read -ra DEV_DEPS_ARRAY <<< "$DEV_DEPENDENCIES"
    for dep in "${DEV_DEPS_ARRAY[@]}"; do
        dep=$(echo $dep | xargs)  # Trim whitespace
        if [ -n "$dep" ]; then
            uv add --dev "$dep"
        fi
    done
fi

# Sync to install everything
echo "Syncing dependencies..."
uv sync

echo ""
echo "Project '$PROJECT_NAME' initialized successfully with UV!"
echo ""
echo "Next steps:"
echo "1. cd $PROJECT_NAME"
echo "2. uv run python -m pip list  # Check installed packages"
echo "3. Add your code to the project"
echo "4. uv run python main.py      # Run your project"