import json
import jsonlines
from typing import List, Any, Dict, Union, Generator

def save_jsonl(data:Union[List[Dict[str,Any]],Dict[str,Any]], loc:str) -> None:

    if isinstance(data, list):
        with jsonlines.open(loc, 'w') as writer:
            writer.write_all(data)
    elif isinstance(data, dict):
        with open(loc, 'a') as f:
            f.write(json.dumps(data) + '\n')
    else:
        raise NotImplementedError()

def load_jsonl(loc:str) -> List[Dict[str,Any]]:
    with open(loc, 'r', encoding='utf-8') as f:
        records = [json.loads(line) for line in f if line.strip()]

    return records

def load_jsonl_generator(loc:str) -> Generator[Dict[str, Any], None, None]:
    with open(loc, 'r', encoding='utf-8') as f:
        for line in f :
            if line.strip():
                yield json.loads(line)

def save_jsonl_append(loc:str, data:Dict[str, Any]) -> None:
    with open(loc, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data) + '\n')
