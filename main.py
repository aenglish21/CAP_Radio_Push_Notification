import os
import time
import winsound
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

CONFIG_FILE = "config.json"  #Config File

class FileUpdateHandler(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config

    def on_modified(self, event):
        if not event.is_directory and event.src_path == self.config["target_file"]:
            print(f"Target file {event.src_path} has been updated.")
            sound_file_path = self.config["sound_file"]
            winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "target_folder": "C:/Users/aenglish/Desktop/CAPDIRECT-Alarm",
            "target_file": "messages.db",
            "sound_file": "C:/Users/aenglish/Downloads/AOl You Got Mail.wav"
        }
        with open(CONFIG_FILE, "w") as config_file:
            json.dump(default_config, config_file, indent=4)
        return default_config

    with open(CONFIG_FILE, "r") as config_file:
        config = json.load(config_file)
    return config

if __name__ == "__main__":
    config = load_config()

    target_folder = config["target_folder"]
    target_file = os.path.join(target_folder, config["target_file"])

    event_handler = FileUpdateHandler(config)
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
