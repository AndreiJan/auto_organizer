import os
from pathlib import Path 

dir_path = Path("C:/Users/Andrei/Downloads")

# print("Files and directories in the current directory:")


images = []
installers = []
zips = []
documents = []
source_code = []
misc = []



for item in dir_path.iterdir():
    # Appends item to the Pictures 
    root, extension = os.path.splitext(item)
    if extension.lower().endswith(("jpg", "jpeg", "png", "gif", "webp", "tiff", "tif","svg", "bmp", "ico", "heic", "avif", "raw")):
        print(f"Appending item to IMAGES")
        images.append(item)

    #Appends item to installers - organizes and places in the installers directory 
    elif extension.lower().endswith((    "exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
        print(f"Appending item to INSTALLERS: {item}")
        installers.append(item)

    #Appends items to the ZIPS array - organizes and places it if it is a ZIP file. Luckily the name isn't too huge
    elif extension.lower().endswith(('.zip')):
        print(f"Appending item to ZIPS: {item}")
        zips.append(item)
    #Appends items if they are classified as a document file. 
    elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers")):
        print(f"Appending item to Documents: {item}")
        documents.append(item)
    
    #Appends items to Source Code if they are categorized as a "Source Code" file
    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        source_code.append(item)

    elif extension.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"This is a common image format. file: {item}")
        pictures.append(item)





    