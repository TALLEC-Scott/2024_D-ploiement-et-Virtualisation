from typing import Union

from fastapi import FastAPI, UploadFile
import numpy as np

import cv2

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greet/")
def greet_person(who: Union[str, None] = None):
    return {"Hello": who}


@app.post("/imgshape/")
async def imgshape(file: UploadFile):
    width = height = depth = 0
    bytes_as_np_array = np.frombuffer(await file.read(), dtype=np.uint8)
    try:
        img = cv2.imdecode(bytes_as_np_array, cv2.IMREAD_COLOR)
        if img is not None:
            height, width, depth = img.shape
    except Exception as e:
        return {"error": str(e)}

    return {"width": width, "height": height, "depth": depth}
