import os
import shutil
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadFolderHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in downloads_folder.glob("*.*"):
            file_extension = file.suffix.lower()
            destination_folder = documents_folder / file_extension[1:]

            if not destination_folder.exists():
                destination_folder.mkdir()

            destination_file_path = destination_folder / file.name

            if destination_file_path.exists():
                new_filename = get_new_filename(destination_folder, file)
                destination_file_path = destination_folder / new_filename

            try:
                shutil.move(str(file), str(destination_file_path))
                print(f"{file.name} áthelyezve a {destination_file_path} fájlba.")
            except Exception as e:
                print(f"{file.name} áthelyezése sikertelen: {str(e)}")

def get_new_filename(destination_folder, file):
    file_base = file.stem
    file_extension = file.suffix.lower()
    counter = 1

    new_filename = f"{file_base}_{counter}{file_extension}"
    new_file_path = destination_folder / new_filename

    while new_file_path.exists():
        counter += 1
        new_filename = f"{file_base}_{counter}{file_extension}"
        new_file_path = destination_folder / new_filename

    return new_filename

# Cseréld le ezeket a mappákat a saját elérési útvonalaidra
downloads_folder = Path("C:/Users/viccelek/valami")
documents_folder = Path("C:/Users/viccelek/Documents")

# Watchdog setup
event_handler = DownloadFolderHandler()
observer = Observer()
observer.schedule(event_handler, str(downloads_folder), recursive=False)
observer.start()



try:
    print("Figyelés elindult...Nyomjon 'CTRL+C'-t a kilépéshez!!")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\nFigyelés megszakítva.")
observer.join()
