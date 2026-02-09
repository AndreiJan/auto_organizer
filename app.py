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
            logger.info(f"New file Detected: {event.src_path}")
            root, extension = os.path.splitext(event.src_path)

            # moves the file to PICTURE directory
            if extension.lower().endswith(("jpg", "jpeg", "png", "gif", "webp", "tiff", "tif","svg", "bmp", "ico", "heic", "avif", "raw")):
                try: 
                    # Removes the file if it already exists
                    if os.path.exists(PICT_DIR, event.src_path):
                        os.remove(PICT_DIR, event.src_path)
                     #It will remove the old one, but keep the same one. Removes redundancy and keeps the latest "document"
                    shutil.move(event.src_path, PICT_DIR)
                    logger.info(f"{event.src_path} moved to IMAGES")
                except: 
                    logger.error(f"Could not move {event.src_path} to {PICT_DIR}")

            # moves the file to INSTALLER directory 
            elif extension.lower().endswith(("exe", "msi", "msu", "msp", "appx","dmg", "pkg","apk", "ipa","deb", "rpm", "sh", "run")):
                try: 
                    if os.path.exists(INST_DIR, event.src_path):
                        os.remove(INST_DIR, event.src_path)
                    shutil.move(event.src_path, INST_DIR)
                    logger.info(f"{event.src_path} moved to INSTALLERS")
                except: 
                    logger.error(f"Could not move {event.src_path} to {INST_DIR}")

            # Moves all ZIP files to the ZIP folder 
            elif extension.lower().endswith(('.zip')):
                try: 
                    if os.path.exists(ZIPS_DIR, event.src_path):
                        os.remove(ZIPS_DIR, event.src_path)
                    shutil.move(event.src_path, ZIPS_DIR)
                    logger.info(f"{event.src_path} moved to ZIPS")
                except: 
                    logger.error(f"Could not move {event.src_path} to {ZIPS_DIR}")
                    
            # Moves all files to the DOCUMENTS folder
            elif extension.lower().endswith(("doc", "docx", "pdf", "txt", "rtf","odt", "xls", "xlsx", "ppt", "pptx", "csv", "pages", "key", "numbers","twb")):
                try:
                    if os.path.exists(DOCT_DIR, event.src_path):
                        os.remove(DOCT_DIR, event.src_path)
                    shutil.move(event.src_path, DOCT_DIR)
                    logger.info(f"{event.src_path} moved to DOCUMENTS")
                except: 
                    logger.error(f"Could not move {event.src_path} to {DOCT_DIR}")

            # Moves all code thingies into a thing
            elif extension.lower().endswith(("py", "js", "ts", "c", "cpp", "h", "cs", "java", "rb", "php", "go", "rs", "swift", "kt", "html", "css", "sql", "sh", "bat", "yml", "json","pem", "pub")):
                try:
                    if os.path.exists(SRCD_DIR, event.src_path):
                        os.remove(SRCD_DIR, event.src_path)
                    shutil.move(event.src_path, SRCD_DIR)
                    logger.info(f"{event.src_path} moved to SOURCE CODE")
                except: 
                    logger.error(f"Could not move {event.src_path} to {SRCD_DIR}")

            # Moves all files into a VIDEO directory
            elif extension.lower().endswith(('.mp4', '.mov', '.mkv', '.avi', '.wmi', '.flv')):
                try:
                    if os.path.exists(VIDE_DIR, event.src_path):
                        os.remove(VIDE_DIR, event.src_path)
                    shutil.move(event.src_path, VIDE_DIR)                
                    logger.info(f"{event.src_path} moved to VIDEOS")
                except: 
                    logger.error(f"Could not move {event.src_path} to {VIDE_DIR}")

            # Moves the files into the MISC folder 
            else:
                try:
                    if os.path.exists(MISC_DIR, event.src_path):
                        os.remove(MISC_DIR, event.src_path)
                    shutil.move(event.src_path, MISC_DIR)
                    logger.info(f"{event.src_path} moved to MISC")
                except: 
                    logger.error(f"Could not move {event.src_path} to {MISC_DIR}")
                



def initial_sweep(watch_path, handler_instance):
    print("Performing initial sweep of the folder...")
    for filename in os.listdir(watch_path):
        file_path = os.path.join(watch_path, filename)
        
        if os.path.isfile(file_path):
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