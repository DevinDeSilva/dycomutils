# dycomutils

[![PyPI version](https://img.shields.io/pypi/v/dycomutils.svg)](https://pypi.org/project/dycomutils/)
[![Python versions](https://img.shields.io/pypi/pyversions/dycomutils.svg)](https://pypi.org/project/dycomutils/)
[![CI](https://github.com/DevinDeSilva/dycomutils/actions/workflows/python-publish.yml/badge.svg)](https://github.com/DevinDeSilva/dycomutils/actions/workflows/python-publish.yml)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/dycomutils?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/dycomutils)


`dycomutils` is a small Python utility package for common day-to-day helpers that show up across scripts and projects.

The library currently focuses on:

- serialization helpers for JSON, JSONL, pickle, and text files
- lightweight concurrency utilities for running named jobs in parallel
- recursive config creation with attribute-style access
- simple graph grouping helpers for connected components
- keystroke automation utilities for typing file contents

This package is a practical toolbox: small functions, minimal ceremony, and utilities that are easy to reuse in notebooks, scripts, and internal tools.

## Installation

Install the package locally:

```bash
pip install .
```

If you want to use the automation helpers or progress-aware concurrency helpers, you may also need:

```bash
pip install pynput tqdm
```

## Package Layout

```text
dycomutils/
  serialization/
  concurrancy/
  config/
  grouping/
  automation/
```

Top-level imports:

```python
import dycomutils

dycomutils.serialization
dycomutils.concurrancy
dycomutils.config
dycomutils.grouping
```

## Functionality

### Serialization

The [`dycomutils/serialization/__init__.py`](/home/desild/work/personal/dycomutils/dycomutils/serialization/__init__.py) module provides compact file I/O helpers for common formats:

- `save_json(data, loc)`
- `load_json(loc)`
- `save_pickle(obj, loc)`
- `load_pickle(loc)`
- `save_text(s, loc)`
- `load_text(loc)`
- `save_jsonl(data, loc)`
- `save_jsonl_append(loc, data)`
- `load_jsonl(loc)`
- `load_jsonl_generator(loc)`
- `file_exist(*args)`

Example:

```python
from dycomutils.serialization import (
    save_json,
    load_json,
    save_jsonl,
    save_jsonl_append,
    load_jsonl_generator,
)

payload = {"name": "example", "version": 1}
save_json(payload, "config.json")

loaded = load_json("config.json")

records = [{"id": 1}, {"id": 2}]
save_jsonl(records, "data.jsonl")
save_jsonl_append("data.jsonl", {"id": 3})

for row in load_jsonl_generator("data.jsonl"):
    print(row)
```

Good fit for:

- experiment metadata
- cached intermediate results
- simple local persistence
- appending one JSON object at a time into a JSONL log
- streaming line-by-line JSONL reads

### Concurrency

The [`dycomutils/concurrancy/__init__.py`](/home/desild/work/personal/dycomutils/dycomutils/concurrancy/__init__.py) module includes `concurrent_dict_execution`, a helper for running a function across a dictionary of named jobs using threads or processes.

It supports:

- thread or process execution
- positional argument jobs
- keyword argument jobs
- progress reporting with `tqdm`
- yielding results together with the original job key

Example with positional arguments:

```python
from dycomutils.concurrancy import concurrent_dict_execution

def add(a, b):
    return a + b

jobs = {
    "first": [1, 2],
    "second": [10, 5],
}

for name, result in concurrent_dict_execution(add, jobs, executor="thread", num_max_workers=2):
    print(name, result)
```

Example with keyword arguments:

```python
jobs = {
    "job_a": {"a": 3, "b": 4},
    "job_b": {"a": 7, "b": 8},
}
```

This is especially useful when you want a lightweight alternative to writing your own `ThreadPoolExecutor` boilerplate each time.

### Config Creation

The [`dycomutils/config/dict_to_config.py`](/home/desild/work/personal/dycomutils/dycomutils/config/dict_to_config.py) module provides `ConfigDict`, a `dict` subclass that turns nested dictionaries into attribute-accessible config objects.

Features:

- access values with `config.key`
- still behaves like a normal dictionary
- recursively converts nested dictionaries
- preserves nested lists and tuples while converting inner dictionaries

Example:

```python
from dycomutils.config import ConfigDict

cfg = ConfigDict({
    "model": {
        "name": "baseline",
        "hidden_size": 256,
    },
    "train": {
        "batch_size": 32,
    },
})

print(cfg.model.name)
print(cfg["train"].batch_size)

cfg.train.epochs = 5
```

This is handy for:

- lightweight configuration objects
- experiment settings
- script parameters
- nested dictionaries that are easier to read with dot access

### Grouping / Connected Components

The [`dycomutils/grouping/__init__.py`](/home/desild/work/personal/dycomutils/dycomutils/grouping/__init__.py) module contains a small union-find implementation:

- `findParent(parent, x)`
- `unionSets(parent, x, y)`
- `getComponents(V, edges)`

`getComponents(V, edges)` returns connected components for an undirected graph represented by:

- `V`: number of vertices
- `edges`: pairs of connected node indices

Example:

```python
from dycomutils.grouping import getComponents

components = getComponents(
    6,
    [
        (0, 1),
        (1, 2),
        (3, 4),
    ],
)

print(components)
# Example output: [[0, 1, 2], [3, 4], [5]]
```

This is useful for basic clustering, graph partitioning, and grouping related indices.

### Automation

The [`dycomutils/automation/keystrokes.py`](/home/desild/work/personal/dycomutils/dycomutils/automation/keystrokes.py) module provides a small CLI utility that reads a file and types its contents using simulated keyboard input.

Capabilities:

- configurable startup delay
- configurable per-character and per-line delays
- randomized timing to make typing less uniform

Example CLI usage:

```bash
python -m dycomutils.automation.keystrokes notes.txt --delay-start 6 --delay-char 0.02 --delay-line 0.5 --random 3
```

This is best suited for local automation workflows where text needs to be replayed as keyboard input.

## Notes

- The concurrency module is exposed as `concurrancy`, matching the current package name in the code.
- The automation module depends on `pynput`.
- The concurrency helper uses `tqdm` for progress display.
- The top-level package exports `serialization`, `concurrancy`, `grouping`, and `config`.

## Positioning

`dycomutils` is best described as a personal general-purpose Python utility package rather than a framework. It packages together reusable helpers for:

- persistence and serialization
- parallel job execution
- config ergonomics
- lightweight graph grouping
- small automation tasks

If you have lots of one-off scripts, research code, data workflows, or internal tooling, this package gives you a single place for the small utilities you end up rewriting over and over.
