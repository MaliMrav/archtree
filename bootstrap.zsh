#!/usr/bin/env zsh
#
# bootstrap.zsh

###############################################################################
# archtree Project Bootstrap
#
###############################################################################

set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-$(pwd)}"

###############################################################################
# Pretty printing
###############################################################################

info() {
    printf "\033[1;34m==>\033[0m %s\n" "$1"
}

success() {
    printf "\033[1;32m✔\033[0m %s\n" "$1"
}

warn() {
    printf "\033[1;33m⚠\033[0m %s\n" "$1"
}

###############################################################################
# Helpers
###############################################################################

create_dir() {

    local dir="$PROJECT_ROOT/$1"

    if [[ -d "$dir" ]]; then
        warn "Directory exists : $1"
    else
        mkdir -p "$dir"
        success "Created directory : $1"
    fi
}

create_file() {

    local file="$PROJECT_ROOT/$1"

    if [[ -f "$file" ]]; then
        warn "File exists      : $1"
    else
        touch "$file"
        success "Created file     : $1"
    fi
}

create_file_with_header() {
    local file="$PROJECT_ROOT/$1"

    if [[ ! -f "$file" ]]; then
        cat > "$file" <<EOF
###############################################################################
# $2
# Copyright (c) 2026 Vladimir Lekic
###############################################################################
EOF
        success "Created file     : $1"
    else
        warn "File exists      : $1"
    fi
}

###############################################################################
# Main
###############################################################################

info "Project root"

echo "    $PROJECT_ROOT"
echo

###############################################################################
# Directories
###############################################################################

info "Creating directories"

create_dir "src"
create_dir "src/archtree"
create_dir "tests"
create_dir "tests/fixtures"

echo

###############################################################################
# Top-level files
###############################################################################

info "Creating top-level files"

create_file ".gitignore"
create_file "LICENSE"
create_file "README.md"
create_file "VERSION"
create_file "pyproject.toml"

echo

###############################################################################
# Python package
###############################################################################

info "Creating Python package"

create_file_with_header "src/archtree/__init__.py" "Python package initializer"
create_file_with_header "src/archtree/__main__.py" "Main entry point for the package"

create_file_with_header "src/archtree/cli.py" "Command-line interface"
create_file_with_header "src/archtree/roles.py" "Role management and permissions"
create_file_with_header "src/archtree/tree.py" "Data structure for tree representation"
create_file_with_header "src/archtree/renderer.py" "Rendering logic for tree visualization"
create_file_with_header "src/archtree/sorting.py" "Sorting algorithms for tree nodes"
create_file_with_header "src/archtree/architectures.py" "Architecture definitions and management"
create_file_with_header "src/archtree/models.py" "Data models for tree nodes and related structures"
create_file_with_header "src/archtree/config.py" "Configuration management and settings"

echo

###############################################################################
# Tests
###############################################################################

info "Creating test files"

create_file_with_header "tests/test_sorting.py" "Tests for sorting algorithms"
create_file_with_header "tests/test_renderer.py" "Tests for rendering logic"
create_file_with_header "tests/test_architectures.py" "Tests for architecture definitions and management"
create_file_with_header "tests/test_roles.py" "Tests for role management"
create_file_with_header "tests/fixtures/__init__.py" "Test fixtures"

echo

###############################################################################
# Initialise files
###############################################################################

info "Initialising VERSION"

VERSION_FILE="$PROJECT_ROOT/VERSION"

if [[ ! -s "$VERSION_FILE" ]]; then
    echo "0.1.0" > "$VERSION_FILE"
    success "Initialised VERSION"
else
    warn "VERSION already initialised"
fi

echo
success "Bootstrap complete."
echo

cat <<EOF
Project structure:

archtree/
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   └── archtree/
│       ├── __init__.py
│       ├── __main__.py
│       │
│       ├── cli.py
│       ├── roles.py
│       ├── tree.py
│       ├── renderer.py
│       ├── sorting.py
│       ├── architectures.py
│       ├── models.py
│       └── config.py
│
└── tests/
    ├── test_roles.py
    ├── test_sorting.py
    ├── test_renderer.py
    ├── test_architectures.py
    └── fixtures/
EOF