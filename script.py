import cv2
import json
import os

def extractImageData(inputimage, outputjson):
    image = cv2.imread(inputimage)

    if image is not None:
        filename = os.path.basename(inputimage)
        height, width = image.shape[:2]
        channels = image.shape[2]

        metadata = {
            "filename": filename,
            "height": height,
            "width": width,
            "channels": channels
        }
        with open(outputjson, 'w') as outfile:
            json.dump(metadata, outfile)


if __name__ == "__main__":
    filename = "/app/external_file"
    outputjson = "/app/output/output.json"
    extractImageData(filename, outputjson)
