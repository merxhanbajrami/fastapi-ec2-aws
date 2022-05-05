from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"who": "Hi there, we are LokaFold Team!"}


@app.get("/teammates")
def get_teammates():
    return {
        "teammates": ['merxhan', 'martin', 'ivona', 'dona', 'juan p.', 'juan v.', 'nicolas', 'stefan']
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
