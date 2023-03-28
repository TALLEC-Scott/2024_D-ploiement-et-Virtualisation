import os
import configparser
import cv2
import numpy as np
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


#iterate for every *.jpg
directory = "/data/input"

for image in os.listdir(directory):
    filepath = os.path.join(directory, image)
    if os.path.isfile(filepath) and (filename.endswith(".jpg") or filename.endswith(".jpeg")):
        # Read the document page image.
        input_image_path = "/data/input/jo-sample1.jpg"
        image = cv2.imread(input_image_path, 1)

        # Init empty page content. 
        # This object will be updated by the ocr pipeline. id can be any string and it is used to identify the page.
        page_layout = PageLayout(id=input_image_path,
             page_size=(image.shape[0], image.shape[1]))

        # Process the image by the OCR pipeline
        page_layout = page_parser.process_page(image, page_layout)

        # Save output
        page_layout.to_altoxml('/data/output/jo-sample1.ALTO.xml') # Save results as ALTO XML.

        # Bonus: display the transcription in the console
        print("Transcription:")
        print("="*50)
        for region in page_layout.regions:
          for line in region.lines:
            print(line.transcription)
        print("="*50)
