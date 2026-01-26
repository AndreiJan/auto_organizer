import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import yaml
import logging.config
import shutil

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

user_profile = os.getenv('USERPROFILE')
path_to_watch = os.path.join(user_profile, 'Downloads')

organized_paths = {}

for key, folder_name in config['paths'].items():
    full_path = os.path.join(path_to_watch, os.path.basename(folder_name))
    
    os.makedirs(full_path, exist_ok=True)
    organized_paths[key] = full_path
    print(f"Ready: {full_path}")

class NewFileHandler(FileSystemEventHandler):
    # This function runs whenever a file or folder is created
    def on_created(self, event):
        if not event.is_directory:
            # print(f"BINGO! New file detected: {event.src_path}") 
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
            elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers","twb")):
                # print(f"Appending item to Documents: {event.src_path}")
                # documents.append(event.src_path)
                shutil.move(event.src_path, DOCT_DIR)
                logger.info(f"{event.src_path} moved to DOCUMENTS")

            
            #Appends items to Source Code if they are categorized as a "Source Code" file
            elif extension.lower().endswith(("py", "js", "ts", "c", "cpp", "h", "cs", "java", "rb", "php", "go", "rs", "swift", "kt", "html", "css", "sql", "sh", "bat", "yml", "json","pem", "pub")):
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
                



def initial_sweep(watch_path, handler_instance):
    print("Performing initial sweep of the folder...")
    # List everything in the directory
    for filename in os.listdir(watch_path):
        file_path = os.path.join(watch_path, filename)
        
        # We only want to move files, and we must ignore the organized folders
        if os.path.isfile(file_path):
            # We manually trigger the on_created logic
            # We create a fake "event" object that watchdog expects
            class MockEvent:
                def __init__(self, src_path):
                    self.src_path = src_path
                    self.is_directory = False
            
            handler_instance.on_created(MockEvent(file_path))
    print("Sweep complete. Starting live monitoring...")
handler = NewFileHandler()
initial_sweep(path_to_watch, handler)
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