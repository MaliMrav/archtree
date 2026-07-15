# archtree

Software is designed by architecture, not by alphabetical order.

Traditional tree viewers display filesystems.

**archtree** displays software architecture.

It presents source trees in architectural order, helping developers understand the public structure of a project before its implementation.

> **Architecture precedes implementation.**

---

## Why?

Most tree viewers answer the question:

> **"Where are my files?"**

**archtree** answers a different question:

> **"How is my software organised?"**

Instead of displaying files alphabetically, **archtree** groups them according to their architectural role.

```text
Public Interface
Implementation
Subcomponents
Other Files
```

The result is a directory tree that reflects how software is designed, rather than simply how it is stored.

---

## Philosophy

Every component should be understood from the outside in.

For each directory, **archtree** presents files in the following order:

1. **Public Interface**
2. **Implementation**
3. **Subcomponents**
4. **Other Files**

This encourages developers to understand a component's public contract before examining its implementation.

> **Architecture precedes implementation.**

---

## Example

Given a traditional filesystem layout:

```text
screens/
├── BootScreen.cpp
├── BootScreen.h
├── CalibrationScreen.cpp
├── CalibrationScreen.h
├── ScreenConfig.h
├── WeatherScreen.cpp
├── WeatherScreen.h
└── control/
    ├── ControlPanelPage.h
    ├── ControlPanelScreen.cpp
    ├── ControlPanelScreen.h
    ├── capabilities/
    │   ├── ConnectivityPage.cpp
    │   └── ConnectivityPage.h
    └── information/
        ├── AboutPage.cpp
        ├── AboutPage.h
        ├── SystemPage.cpp
        └── SystemPage.h
```

`archtree` renders:

```text
../screens/
├── BootScreen.h
├── CalibrationScreen.h
├── ScreenConfig.h
├── WeatherScreen.h
├── BootScreen.cpp
├── CalibrationScreen.cpp
├── WeatherScreen.cpp
└── control/
    ├── ControlPanelPage.h
    ├── ControlPanelScreen.h
    ├── ControlPanelScreen.cpp
    ├── capabilities/
    │   ├── ConnectivityPage.h
    │   └── ConnectivityPage.cpp
    └── information/
        ├── AboutPage.h
        ├── SystemPage.h
        ├── AboutPage.cpp
        └── SystemPage.cpp
```

Notice that:

- Public interfaces appear before implementations.
- Components appear before their internal subcomponents.
- Directories are distinguished with a trailing `/`.
- The tree naturally reads from architecture to implementation.

---

## Current Status

**Version:** 0.1.1

Current capabilities include:

- Unicode tree rendering
- Architecture-aware sorting
- C/C++ architectural layouts
- Public interfaces before implementations
- Components before subcomponents
- Clean, readable terminal output

---

## Architecture

`archtree` is intentionally built as a pipeline.

```text
Filesystem
    │
    ▼
Tree Construction
    │
    ▼
Architectural Classification
    │
    ▼
Sorting
    │
    ▼
Rendering
```

Each stage has a single responsibility.

This separation keeps the implementation simple while allowing future architectural models to be added without changing the renderer or filesystem traversal.

---

## Installation

Install locally during development:

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

Example:

```bash
archtree ../screens
```

---

## Project Structure

```text
src/
└── archtree/
    ├── __init__.py
    ├── __main__.py
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
| :------ | :------------- |
| `cli.py` | Command-line interface |
| `roles.py` | Architectural role definitions |
| `tree.py` | Filesystem traversal and tree construction |
| `renderer.py` | Unicode tree rendering |
| `sorting.py` | Architecture-aware node ordering |
| `architectures.py` | Architectural role classification |
| `models.py` | Tree data structures |
| `config.py` | Configuration support |

---

## Roadmap

Future development is expected to include:

- Additional language architectures
- Project-specific `.archtree` configuration
- Component statistics
- Theme support
- Additional output formats (JSON, Markdown, Graphviz)
- Colourised output
- Architecture validation

The architecture has been designed so these capabilities can be added without changing the overall processing pipeline.

---

## Design Principles

The project is guided by a small set of engineering principles.

- Architecture precedes implementation.
- Components should be understood from the outside in.
- Every module should have a single responsibility.
- Good architecture should feel inevitable.

These principles influence both the implementation of **archtree** and the way it presents software projects.

---

## License

MIT License.