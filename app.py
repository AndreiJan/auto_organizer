import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import yaml
import logging.config
import shutil

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
ZIPS_DIR = config['paths']['zips']
# Ensures all folders/paths are created and set
# path_to_watch = "F:/programming/auto_organizer/test"


# for folder_path in config['paths'].values():
#     os.makedirs(folder_path, exist_ok=True)
#     print(f"Ensured directory exists: {folder_path}")

# logger.info("All Folders created/verified")


# path_to_watch = "F:/programming/auto_organizer/test"
user_profile = os.getenv('USERPROFILE')
path_to_watch = os.path.join(user_profile, 'Downloads')

# We create a dictionary to hold the dynamic paths
organized_paths = {}

for key, folder_name in config['paths'].items():
    # This creates the path INSIDE your test folder automatically
    # It takes the folder name (e.g., 'pictures') and joins it to 'test'
    full_path = os.path.join(path_to_watch, os.path.basename(folder_name))
    
    os.makedirs(full_path, exist_ok=True)
    organized_paths[key] = full_path
    print(f"Ready: {full_path}")

# Now re-assign your variables using the dynamic dictionary
PICT_DIR = organized_paths['pictures']
INST_DIR = organized_paths['installers']
ZIPS_DIR = organized_paths['zips']
DOCT_DIR = organized_paths['documents']
SRCD_DIR = organized_paths['source_code']
VIDE_DIR = organized_paths['videos']
MISC_DIR = organized_paths['misc']
# Sets all the folders and all 
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
                # images.append(event.src_path)
                shutil.move(event.src_path, PICT_DIR)
                logger.info(f"{event.src_path} moved to IMAGES")

            #Appends item to installers - organizes and places in the installers directory 
            elif extension.lower().endswith(("exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
                # print(f"Appending item to INSTALLERS: {event.src_path}")
                # installers.append(event.src_path)
                shutil.move(event.src_path, INST_DIR)
                logger.info(f"{event.src_path} moved to INSTALLERS")

            #Appends items to the ZIPS array - organizes and places it if it is a ZIP file. Luckily the name isn't too huge
            elif extension.lower().endswith(('.zip')):
                # print(f"Appending item to ZIPS: {event.src_path}")
                # zips.append(event.src_path)
                shutil.move(event.src_path, ZIPS_DIR)
                logger.info(f"{event.src_path} moved to ZIPS")
                
            #Appends items if they are classified as a document file. 
            elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers")):
                # print(f"Appending item to Documents: {event.src_path}")
                # documents.append(event.src_path)
                shutil.move(event.src_path, DOCT_DIR)
                logger.info(f"{event.src_path} moved to DOCUMENTS")

            
            #Appends items to Source Code if they are categorized as a "Source Code" file
            elif extension.lower().endswith(("py", "js", "ts", "c", "cpp", "h", "cs", "java", "rb", "php", "go", "rs", "swift", "kt", "html", "css", "sql", "sh", "bat", "yml", "json")):
                # print(f"Appending item to source_code: {event.src_path}")
                # documents.append(event.src_path)
                shutil.move(event.src_path, SRCD_DIR)
                logger.info(f"{event.src_path} moved to SOURCE CODE")


            elif extension.lower().endswith(('.mp4', '.mov', '.mkv', '.avi', '.wmi', '.flv')):
                shutil.move(event.src_path, VIDE_DIR)                
                logger.info(f"{event.src_path} moved to VIDEOS")
            else:
                # print(f"This is a common image format. file: {item}")
                # misc.append(event.src_path)
                shutil.move(event.src_path, MISC_DIR)
                logger.info(f"{event.src_path} moved to MISC")
                



# --- Setup and Start ---
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