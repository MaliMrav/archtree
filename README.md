# archtree

Software is organised by architecture.

Most tree viewers display filesystems.

Those are not the same thing.

**archtree** displays source trees in architectural order, helping you understand the public structure of a project before its implementation.

> **Architecture precedes implementation.**

---

Display source trees in **architectural order** rather than filesystem order.

Traditional tree viewers answer:

> **"Where are my files?"**

**archtree** answers:

> **"How is my software organised?"**

Instead of displaying files alphabetically, **archtree** groups them according to their architectural role.

```
Public Interface
Implementation
Subcomponents
```

The result is a directory tree that reflects how software is designed, not merely how it is stored.

---

## Why?

Most tree viewers sort files alphabetically.

For many languages—particularly C and C++—this means implementation files (`.cpp`) often appear before their corresponding public interfaces (`.h`).

For example:

```text
BootScreen.cpp
BootScreen.h
```

Architecturally, however, the interface comes first.

```text
BootScreen.h
BootScreen.cpp
```

When browsing a project, developers usually want to understand the public API before reading its implementation.

**archtree** makes that architectural relationship explicit.

---

## Philosophy

Every directory represents a component.

Each component is presented in the following order:

1. **Public Interface**
2. **Implementation**
3. **Subcomponents**
4. **Other Files**

This follows a simple principle:

> **Architecture precedes implementation.**

---

## Example

Instead of this:

```text
screens
├── BootScreen.cpp
├── BootScreen.h
├── CalibrationScreen.cpp
├── CalibrationScreen.h
└── control
```

**archtree** produces:

```text
screens
├── BootScreen.h
├── CalibrationScreen.h
├── BootScreen.cpp
├── CalibrationScreen.cpp
└── control
```

The output naturally reads from interface to implementation.

---

## Features

- Architecture-aware source tree display
- Public interfaces shown before implementations
- Components shown before subcomponents
- Language-specific architecture definitions
- Clean Unicode tree output
- Extensible architecture model
- Configurable project rules

---

## Planned Language Support

The architecture model is language-independent.

Initial support is planned for:

- C
- C++
- Python
- Go
- Rust

Additional languages can be added by defining new architecture mappings.

---

## Installation

```bash
pip install .
```

---

## Usage

Display the current directory:

```bash
archtree
```

Display a specific directory:

```bash
archtree path/to/project
```

Future versions will support additional options such as:

```bash
archtree --architecture cpp
archtree --depth 2
archtree --all
```

---

## Project Structure

```text
src/
└── archtree/
    ├── cli.py
    ├── roles.py
    ├── tree.py
    ├── renderer.py
    ├── sorting.py
    ├── architectures.py
    ├── models.py
    └── config.py
```

Each module has a single responsibility.

| Module | Responsibility |
|---------|----------------|
| `cli.py` | Command-line interface |
| `roles.py` | Architectural role definitions |
| `tree.py` | Filesystem traversal |
| `renderer.py` | Tree rendering |
| `sorting.py` | Architectural ordering |
| `architectures.py` | Language-specific architecture definitions |
| `models.py` | Tree data structures |
| `config.py` | Project configuration |

---

## Roadmap

Planned capabilities include:

- Multiple language architectures
- Project-specific `.archtree` configuration
- JSON output
- Markdown output
- Graphviz export
- Git status integration
- Colourised output
- Architecture validation
- Component statistics

---

## License

MIT License.