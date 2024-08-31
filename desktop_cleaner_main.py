# project requirements
#   track desktop, if new file is added then move it to the right location
#   find type of file that has been added
#   run in background
#   file organization: each file on desktop is moved in folder base on its format (audio, video, image, pdf document,
#                      each folder contains year and month subfolders in which the file is moved based on creation date)
import time
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import os
import json
import shutil

# This defines a new class MyHandler that extends the FileSystemEventHandler class.
# By inheriting from FileSystemEventHandler, MyHandler can override specific methods
# to handle different types of file system events (e.g., modifications, creations, deletions).
class MyHandler(FileSystemEventHandler):
    # This method is called automatically whenever a file or directory is modified in the monitored directory.
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i=1

