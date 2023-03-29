from typing import Union

from fastapi import FastAPI, UploadFile, HTTPException, Response
import numpy as np
import os
import configparser
import cv2
from pero_ocr.document_ocr.layout import PageLayout
from pero_ocr.document_ocr.page_parser import PageParser

# Read config file.
config_path = "./config_cpu.ini"
config = configparser.ConfigParser()
config.read(config_path)

# Init the OCR pipeline.
# You have to specify config_path to be able to use relative paths
# inside the config file.
page_parser = PageParser(config, config_path=os.path.dirname(config_path))

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
    img = cv2.imdecode(bytes_as_np_array, cv2.IMREAD_COLOR)

    if img is not None:
        height, width, depth = img.shape
    else:
        raise HTTPException(status_code=500, detail="Cannot find image data in file '" + file.filename + "'.")

    return {"width": width, "height": height, "depth": depth}

@app.post("/process_image/")
async def process_image(file: UploadFile):

    width = height = depth = 0
    bytes_as_np_array = np.frombuffer(await file.read(), dtype=np.uint8)
    img = cv2.imdecode(bytes_as_np_array, cv2.IMREAD_COLOR)

    if img is not None:
        height, width, depth = img.shape
    else:
        raise HTTPException(status_code=500, detail="Cannot find image data in file '" + file.filename + "'.")

    # Init empty page content.
    # This object will be updated by the ocr pipeline. id can be any string and it is used to identify the page.
    page_layout = PageLayout(id="id",
         page_size=(img.shape[0], img.shape[1]))

    # Process the image by the OCR pipeline
    page_layout = page_parser.process_page(img, page_layout)


    # Save output
    page_layout.to_altoxml("output.txt") # Save results as ALTO XML.
    # Bonus: display the transcription in the console

    text_file = open("output.txt", "r")
    data = text_file.read()
    text_file.close()
    print("Transcription:")
    print("="*50)
    for region in page_layout.regions:
      for line in region.lines:
        print(line.transcription)
    print("="*50)


    return Response(content=data, media_type="application/xml")
