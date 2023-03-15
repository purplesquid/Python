import os
from PIL import Image

directory = ""
fullPath = "" + directory

def combine(name, jpg, chapter):
    pdfPath = "" + directory + r"/"
    pdfName = pdfPath + name + ".pdf"
    
    images = [
        Image.open(chapter + r"/" + str(f) + ".jpg")
        for f in range(1,jpg+1)
    ]

    images[0].save(
        pdfName, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )

def main():
    for folder in os.listdir(fullPath):
        chapter = os.path.join(fullPath,folder)
        jpgCount = 0
        
        for file in os.listdir(chapter):
            jpgCount = jpgCount + 1
            
        combine(folder, jpgCount, chapter)

if __name__ == "__main__":
    main()
