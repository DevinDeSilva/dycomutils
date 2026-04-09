import os

from .json import load_json, save_json
from .jsonl import load_jsonl, load_jsonl_generator, save_jsonl, save_jsonl_append
from .pickle import load_pickle, save_pickle
from .text import load_text, save_text

__all__ = [
    "save_json",
    "load_json",
    "save_jsonl",
    "save_jsonl_append",
    "load_jsonl",
    "load_jsonl_generator",
    "save_pickle",
    "load_pickle",
    "save_text",
    "load_text",
    "file_exist",
]


def file_exist(*args) -> bool:
    return os.path.exists(os.path.join(*args))
    
