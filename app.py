import os
from pathlib import Path 

dir_path = Path("C:/Users/Andrei/Downloads")

# print("Files and directories in the current directory:")


pictures = []
installers = []
zips = []
documents = []
source_code = []
misc = []



for item in dir_path.iterdir():
    # Appends item to the Pictures 
    root, extension = os.path.splitext(item)
    if extension.lower().endswith(("jpg", "jpeg", "png", "gif", "webp", "tiff", "tif","svg", "bmp", "ico", "heic", "avif", "raw")):
        print(f"This is a common image format. file: {item}\nAppending item to pictures array\n{len(pictures)}")
        pictures.append(item)

    #Appends item to installers - organizes and places in the installers directory 
    elif extension.lower().endswith((    "exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
        print(f"This is a common installer files. file: {item}")
        installers.append(item)

    #        
    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        pictures.append(item)




    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        pictures.append(item)
        
    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        pictures.append(item)

    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        pictures.append(item)





    