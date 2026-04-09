import json

def save_json(data:dict, loc:str) -> None:
    with open(loc, "w") as f0:
        json.dump(data, f0)

def load_json(loc:str) -> dict:
    with open(loc,"r") as f0:
        return json.load(f0)