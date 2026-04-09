import pickle
from typing import Any

def load_pickle(loc:str) -> Any:
    with open(loc, "rb") as f0:
        return pickle.load(f0)
    
def save_pickle(obj:Any, loc:str)->None:
    with open(loc, "wb") as f0:
        pickle.dump(obj,f0)