@echo off
REM uv-initialization-script.bat
REM Script to help initialize Python projects with UV on Windows

setlocal enabledelayedexpansion

set "PYTHON_VERSION="
set "DEPENDENCIES="
set "DEV_DEPENDENCIES="
set "INIT_VCS=1"
set "INIT_README=1"
set "PROJECT_NAME="

:parse_args
if "%~1"=="" goto :check_uv
if "%~1"=="-h" goto :show_help
if "%~1"=="--help" goto :show_help
if "%~1"=="-p" (
    set "PYTHON_VERSION=%~2"
    shift
    shift
    goto :parse_args
)
if "%~1"=="--python" (
    set "PYTHON_VERSION=%~2"
    shift
    shift
    goto :parse_args
)
if "%~1"=="-d" (
    set "DEPENDENCIES=%~2"
    shift
    shift
    goto :parse_args
)
if "%~1"=="--deps" (
    set "DEPENDENCIES=%~2"
    shift
    shift
    goto :parse_args
)
if "%~1"=="--dev-deps" (
    set "DEV_DEPENDENCIES=%~2"
    shift
    shift
    goto :parse_args
)
if "%~1"=="--no-vcs" (
    set "INIT_VCS=0"
    shift
    goto :parse_args
)
if "%~1"=="--no-readme" (
    set "INIT_README=0"
    shift
    goto :parse_args
)
set "PROJECT_NAME=%~1"
shift
goto :parse_args

:show_help
echo UV Project Initialization Script for Windows
echo.
echo Usage: %0 [OPTIONS] [PROJECT_NAME]
echo.
echo Options:
echo   -h, --help              Show this help message
echo   -p, --python VERSION    Specify Python version (e.g., 3.11, 3.12)
echo   -d, --deps DEPS         Comma-separated list of dependencies to add
echo   --dev-deps DEPS         Comma-separated list of dev dependencies
echo   --no-vcs               Skip git initialization
echo   --no-readme            Skip README creation
echo.
echo Examples:
echo   %0 my-project                    ^&^& echo Create project with default settings
echo   %0 -p 3.12 my-api              ^&^& echo Create project with Python 3.12
echo   %0 -d "requests,flask" my-web  ^&^& echo Create with dependencies
goto :eof

:check_uv
REM Check if UV is installed
where uv >nul 2>nul
if errorlevel 1 (
    echo Error: UV is not installed. Please install UV first.
    echo Visit: https://github.com/astral-sh/uv
    exit /b 1
)

REM If no project name provided, use current directory name
if "%PROJECT_NAME%"=="" (
    for %%F in (.) do set "PROJECT_NAME=%%~nxF"
    echo Using current directory name: %PROJECT_NAME%
) else (
    REM Create project directory if it doesn't exist
    if not exist "%PROJECT_NAME%" (
        mkdir "%PROJECT_NAME%"
    )
    cd "%PROJECT_NAME%" || exit /b 1
)

echo Initializing Python project: %PROJECT_NAME%

REM Build the init command
set "INIT_CMD=uv init"
if defined PYTHON_VERSION (
    set "INIT_CMD=!INIT_CMD! --python %PYTHON_VERSION%"
)

if "%INIT_VCS%"=="0" (
    set "INIT_CMD=!INIT_CMD! --no-git"
)

if "%INIT_README%"=="0" (
    set "INIT_CMD=!INIT_CMD! --no-readme"
)

%INIT_CMD%

echo Project initialized successfully!

REM Add dependencies if provided
if defined DEPENDENCIES (
    echo Adding dependencies: %DEPENDENCIES%
    for %%a in ("%DEPENDENCIES:,=" "%") do (
        set "dep=%%~a"
        if not "!dep!"=="" (
            uv add "!dep!"
        )
    )
)

REM Add dev dependencies if provided
if defined DEV_DEPENDENCIES (
    echo Adding dev dependencies: %DEV_DEPENDENCIES%
    for %%a in ("%DEV_DEPENDENCIES:,=" "%") do (
        set "dep=%%~a"
        if not "!dep!"=="" (
            uv add --dev "!dep!"
        )
    )
)

REM Sync to install everything
echo Syncing dependencies...
uv sync

echo.
echo Project '%PROJECT_NAME%' initialized successfully with UV!
echo.
echo Next steps:
echo 1. cd %PROJECT_NAME%
echo 2. uv run python -m pip list  ^&^& echo Check installed packages
echo 3. Add your code to the project
echo 4. uv run python main.py      ^&^& echo Run your project