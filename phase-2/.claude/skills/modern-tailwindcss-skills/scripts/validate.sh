#!/bin/bash
# Validation script for modern-tailwindcss-skills

echo "Validating modern-tailwindcss-skills..."

# Check if SKILL.md exists
if [ ! -f "SKILL.md" ]; then
    echo "ERROR: SKILL.md not found"
    exit 1
fi

# Check if required sections exist in SKILL.md
if ! grep -q "Core Capabilities" SKILL.md; then
    echo "ERROR: Core Capabilities section not found in SKILL.md"
    exit 1
fi

if ! grep -q "Implementation Guidelines" SKILL.md; then
    echo "ERROR: Implementation Guidelines section not found in SKILL.md"
    exit 1
fi

if ! grep -q "Quality Standards" SKILL.md; then
    echo "ERROR: Quality Standards section not found in SKILL.md"
    exit 1
fi

if ! grep -q "Validation Checklist" SKILL.md; then
    echo "ERROR: Validation Checklist section not found in SKILL.md"
    exit 1
fi

# Check if references directory exists and has content
if [ ! -d "references" ]; then
    echo "ERROR: references directory not found"
    exit 1
fi

reference_files=$(ls references/*.md | wc -l)
if [ "$reference_files" -lt 3 ]; then
    echo "WARNING: Less than 3 reference files found, consider adding more"
fi

echo "Validation passed! modern-tailwindcss-skills is ready."