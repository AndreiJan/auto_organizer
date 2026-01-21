# import os
# from pathlib import Path 


# """
# TO DO's 
# - Program must scan FILES ONLY in 

# """


# dir_path = Path("C:/Users/Andrei/Downloads")

# # print("Files and directories in the current directory:")


# # Replace with PATHS - Probably after the testing has been confirmed and completed. 
# images = []
# installers = []
# zips = []
# documents = []
# source_code = []
# misc = []
# folders = [images, installers, zips, documents, source_code, misc]


# # Idea - Could potentially require a CLASS for it. Although I am not too sure if that's even needed. 
# # Probably when the idea gets bigger then we can consider it "important"
# for item in dir_path.iterdir():
    # Appends item to the Pictures 
    # root, extension = os.path.splitext(item)
    # if extension.lower().endswith(("jpg", "jpeg", "png", "gif", "webp", "tiff", "tif","svg", "bmp", "ico", "heic", "avif", "raw")):
    #     print(f"Appending item to IMAGES")
    #     images.append(item)

    # #Appends item to installers - organizes and places in the installers directory 
    # elif extension.lower().endswith((    "exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
    #     print(f"Appending item to INSTALLERS: {item}")
    #     installers.append(item)

    # #Appends items to the ZIPS array - organizes and places it if it is a ZIP file. Luckily the name isn't too huge
    # elif extension.lower().endswith(('.zip')):
    #     print(f"Appending item to ZIPS: {item}")
    #     zips.append(item)
    # #Appends items if they are classified as a document file. 
    # elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers")):
    #     print(f"Appending item to Documents: {item}")
    #     documents.append(item)
    
    # #Appends items to Source Code if they are categorized as a "Source Code" file
    # elif extension.lower().endswith(("py", "js", "ts", "c", "cpp", "h", "cs", "java", "rb", "php", "go", "rs", "swift", "kt", "html", "css", "sql", "sh", "bat", "yml", "json")):
    #     print(f"Appending item to source_code: {item}")
    #     source_code.append(item)

    # else:
    #     # print(f"This is a common image format. file: {item}")
    #     misc.append(item)







# # Create a dictionary to map names to your lists
# folders_dict = {
#     "Images": images,
#     "Installers": installers,
#     "Zips": zips,
#     "Documents": documents,
#     "Source Code": source_code,
#     "Misc": misc
# }

# print("\nResults:")
# # One-liner to print names and their lengths
# [print(f"{name}: {len(content)} files") for name, content in folders_dict.items()]

import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import yaml
import logging.config
# Adding Logging event to properly capture the shit that is happening inside the system. 
with open("config/app_log_conf.yml", "r") as f:
    LOG_CONFIG = yaml.safe_load(f.read())
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('basicLogger')


with open("app_conf.yml", "r") as f:
    config = yaml.safe_load(f)

ARCH_DIR = config['paths']['archives']
DOCT_DIR = config['paths']['documents']
INST_DIR = config['paths']['installers']
MUSI_DIR = config['paths']['music']
MISC_DIR = config['paths']['misc']
PICT_DIR = config['paths']['pictures']
SRCD_DIR = config['paths']['source_code']
VIDE_DIR = config['paths']['videos']




# Generally only needs to create the item when needs to be done
class NewFileHandler(FileSystemEventHandler):
    # This function runs whenever a file or folder is created
    def on_created(self, event):
        if not event.is_directory:
            # print(f"BINGO! New file detected: {event.src_path}") #DEBUGGER - 
            logger.info(f"New file Detected: {event.src_path}")
            # Just like the thing, we need to break the file apart
            root, extension = os.path.splitext(event.src_path)
            print(extension)
            if extension.lower().endswith(("jpg", "jpeg", "png", "gif", "webp", "tiff", "tif","svg", "bmp", "ico", "heic", "avif", "raw")):
                # print(f"Appending item to IMAGES")
                logger.info(f"{event.src_path} moved to IMAGES")
                images.append(event.src_path)

            #Appends item to installers - organizes and places in the installers directory 
            elif extension.lower().endswith(("exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
                # print(f"Appending item to INSTALLERS: {event.src_path}")
                logger.info(f"{event.src_path} moved to INSTALLERS")
                installers.append(event.src_path)

            #Appends items to the ZIPS array - organizes and places it if it is a ZIP file. Luckily the name isn't too huge
            elif extension.lower().endswith(('.zip')):
                # print(f"Appending item to ZIPS: {event.src_path}")
                logger.info(f"{event.src_path} moved to ZIPS")
                zips.append(event.src_path)
            #Appends items if they are classified as a document file. 
            elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers")):
                # print(f"Appending item to Documents: {event.src_path}")
                logger.info(f"{event.src_path} moved to DOCUMENTS")
                documents.append(event.src_path)
            
            #Appends items to Source Code if they are categorized as a "Source Code" file
            elif extension.lower().endswith(("py", "js", "ts", "c", "cpp", "h", "cs", "java", "rb", "php", "go", "rs", "swift", "kt", "html", "css", "sql", "sh", "bat", "yml", "json")):
                # print(f"Appending item to source_code: {event.src_path}")
                logger.info(f"{event.src_path} moved to SOURCE CODE")
                source_code.append(event.src_path)

            elif extension.loer().endswith(('.mp4', '.mov', '.mkv', '.avi', '.wmi', '.flv'))
                logger.info(f"{event.src_path} moved to VIDEOS")
            else:
                # print(f"This is a common image format. file: {item}")
                misc.append(event.src_path)


# --- Setup and Start ---
path_to_watch = "C:/Users/Andrei/Downloads"
handler = NewFileHandler()
observer = Observer()

observer.schedule(handler, path_to_watch, recursive=False)
observer.start()

try:
    print(f"Monitoring {path_to_watch}...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("Stopped.")
observer.join()

