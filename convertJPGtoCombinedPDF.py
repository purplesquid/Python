import os
from PIL import Image

def main():
    imagePath = r""
    savePath = r""
    name = ""
    pdfPath = savePath + "\\" + name + ".pdf"
    
    images = [
        Image.open(imagePath + "\\" + f)
        for f in os.listdir(imagePath)
    ]

    images[0].save(
        pdfPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

if __name__ == "__main__":
    main()
