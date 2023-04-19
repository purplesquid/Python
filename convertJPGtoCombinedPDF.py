import os
import numpy as np
from PIL import Image

def sortList(path):

    fileArray = []
    for f in os.listdir(path):
        fileArray.append(sorted(f.split("."))[0]

    npfileArray = np.array(fileArray)
                         
    #Change to int array to sort numbered files
    result = npfileArray.astype(np.int64)
    
    finalSort = sorted(result)
    return finalSort

def main():
    imagePath = r""
    savePath = r""
    name = ""
    pdfPath = savePath + "\\" + name + ".pdf"
    
    images = [
        Image.open(imagePath + "\\" + str(f) + ".JPG")
        for f in sortList(imagePath)
    ]

    images[0].save(
        pdfPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

if __name__ == "__main__":
    main()
