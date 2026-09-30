# RUTINHANTERARE

My first Python project, written in spring 2024 after roughly three months of learning Python.

It is a terminal-based daily routine tracker that asks about wake-up time, habits, activities and training, then turns the answers into a daily score.

The project became a playground for learning:

- classes and inheritance
- mixins
- decorators
- type hints
- unit tests
- interactive CLI input
- simple scoring functions
- parsing Swedish number words into integers

The code and comments are primarily in Swedish.

## Running

```bash
make run
```

or:

```bash
python3 main.py
```

## Verification

```bash
make check
```

The restored project currently has regression coverage for:

- Swedish number-word conversion
- compound numbers
- hundreds and thousands
- invalid numeric input
- Unicode-normalized Swedish input such as `löpning`

## Project lineage

1. `RUTINHANTERARE` — first Python routine tracker, 2024
2. `amor_fati` — restart with package structure and YAML-defined activities, 2025
3. `AmorFatiMVP` — immutable event model and JSONL logging, 2025
4. Django-based successor — later experiment and future continuation

## Historical restoration

The project has been kept close to its original 2024 form.

Small maintenance fixes were made to:

- remove IDE-specific files and old test output
- prevent invalid number words from causing an infinite loop
- normalize Unicode input so Swedish characters work consistently
- add regression coverage for the historical `löpning` input issue
- add a small Makefile for running and verifying the project

The original architecture, naming and overall design were intentionally preserved.

## Status

Historical project, kept as the starting point of the Amor Fati / training-log project line.
