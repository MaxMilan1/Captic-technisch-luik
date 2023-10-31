import cv2
import json
import os

def extractImageData(inputimage, outputjson):
    image = cv2.imread(inputimage)

    if image is not None:
        # filename = os.path.basename(inputimage) not needed since file provided to docker container as external file all files will be named "external_file"
        height, width = image.shape[:2]
        channels = image.shape[2]

        metadata = {
            # "filename": filename,
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
