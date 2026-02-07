@echo off
REM Validation script for modern-tailwindcss-skills

echo Validating modern-tailwindcss-skills...

REM Check if SKILL.md exists
if not exist "SKILL.md" (
    echo ERROR: SKILL.md not found
    exit /b 1
)

REM Check if required sections exist in SKILL.md
findstr /C:"Core Capabilities" SKILL.md >nul
if errorlevel 1 (
    echo ERROR: Core Capabilities section not found in SKILL.md
    exit /b 1
)

findstr /C:"Implementation Guidelines" SKILL.md >nul
if errorlevel 1 (
    echo ERROR: Implementation Guidelines section not found in SKILL.md
    exit /b 1
)

findstr /C:"Quality Standards" SKILL.md >nul
if errorlevel 1 (
    echo ERROR: Quality Standards section not found in SKILL.md
    exit /b 1
)

findstr /C:"Validation Checklist" SKILL.md >nul
if errorlevel 1 (
    echo ERROR: Validation Checklist section not found in SKILL.md
    exit /b 1
)

REM Check if references directory exists and has content
if not exist "references" (
    echo ERROR: references directory not found
    exit /b 1
)

echo Validation passed! modern-tailwindcss-skills is ready.