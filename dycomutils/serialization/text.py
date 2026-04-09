def save_text(s:str, loc:str) -> None:
    with open(loc, "w") as f0:
        f0.write(s)

def load_text(loc:str) -> str:
    with open(loc,"r") as f0:
        return f0.read()