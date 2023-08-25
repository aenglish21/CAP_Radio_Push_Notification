import os
import time
import winsound
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileUpdateHandler(FileSystemEventHandler):
    def __init__(self, target_file):
        self.target_file = target_file

    def on_modified(self, event):
        if not event.is_directory and event.src_path == self.target_file:
            print(f"Target file {event.src_path} has been updated.")
            sound_file_path = "C:/Users/aenglish/Downloads/AOl You Got Mail.wav"  # Corrected sound file path
            winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)

if __name__ == "__main__":
    target_folder = "C:/Users/aenglish/Desktop/CAPDIRECT-Alarm"  # Replace with the actual path to the folder you want to monitor
    target_file = os.path.join(target_folder, "messages.db")  # Replace with the actual target file name

    event_handler = FileUpdateHandler(target_file)
    observer = Observer()
    observer.schedule(event_handler, path=target_folder)
    observer.start()

    print(f"Monitoring file: {target_file}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
