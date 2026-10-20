# 42 Python Modules

**A learning journey through Python, from basic functions to structured data and functional programming.**

This repository brings together the Python modules I worked on as part of the
42 curriculum. These exercises were designed to help me learn Python step by
step, practise core programming concepts, and build a foundation for larger
projects such as [RAG Against the Machine](https://github.com/Rubenex29/RAG)
and [CallMeMaybe](https://github.com/Rubenex29/CallMeMaybe).

The modules are educational exercises. They reflect my learning process and
the constraints of individual assignments, rather than a single application.

## Learning path

| Module | Topics practised |
| --- | --- |
| [Module 00](module00/) | Functions, basic calculations, conditionals, iteration and recursion |
| [Module 01](module01/) | Classes, objects, encapsulation, inheritance and class-level behaviour |
| [Module 02](module02/) | Exceptions, custom errors, raising errors and cleanup with `finally` |
| [Module 03](module03/) | Command-line arguments, lists, tuples, sets, dictionaries and data streams |
| [Module 04](module04/) | Text files, input/output streams, context managers and file error handling |
| [Module 05](module05/) | Abstract base classes, polymorphism and data-processing interfaces |
| [Module 06](module06/) | Packages, imports, module organisation and circular dependencies |
| [Module 07](module07/) | Object-oriented design, interfaces, factories and strategies in a card-game model |
| [Module 08](module08/) | Virtual environments, dependencies and environment-based configuration |
| [Module 09](module09/) | Pydantic models, field constraints and validation across related data |
| [Module 10](module10/) | Lambdas, higher-order functions, closures, `functools` and decorators |

## Exploring the exercises

Each `moduleXX/` directory retains the exercise layout from its original
repository. Most exercises are grouped under `ex0/`, `ex1/`, and so on;
Module 06 uses a package-oriented layout.

Use Python 3 and run examples from the relevant module directory. For example:

```bash
git clone https://github.com/Rubenex29/42-python-modules.git
cd 42-python-modules/module01
python3 ex0/ft_garden_intro.py
```

For Module 07, run the examples as modules so package imports resolve:

```bash
cd 42-python-modules/module07
python3 -m ex0.main
```

Some early exercises define functions intended to be called by a test harness,
so running their files directly may produce no output. File-handling exercises
can create or update files in the current working directory.

There is no shared environment or universal test command for all modules.
Module 08 contains exercise-specific dependency files and an `.env.example`;
Module 09 requires Pydantic 2. Use an isolated virtual environment for exercises
with external dependencies and follow any local configuration files. Keep real
credentials out of Git.

## History and provenance

The default-branch histories of `PythonModule00` through `PythonModule10` were
merged into this repository without rewriting the original commits. Authors,
commit IDs and existing credits are preserved. Each import commit places that
module's original contents under its own directory; older commits retain their
original paths.

The original repositories remain available for course-related use and reference.
This repository provides a single place to browse the full learning sequence.

*Developed as part of the 42 Python curriculum.*
