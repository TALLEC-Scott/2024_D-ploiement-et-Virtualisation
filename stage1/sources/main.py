from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greet/")
def greet_person(who: Union[str, None] = None):
    return {"Hello": who}
