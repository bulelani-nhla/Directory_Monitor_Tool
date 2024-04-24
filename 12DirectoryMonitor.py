import os
import time
import shutil
from datetime import datetime

def monitor_and_copy(directory, destination_directory):
    # Store the current state of the directory
    previous_state = dict([(file, None) for file in os.listdir(directory)])

    while True:
        time.sleep(6)  # Adjust the interval as needed
        current_state = dict([(file, None) for file in os.listdir(directory)])

        # Check for new files
        new_files = [file for file in current_state if file not in previous_state]
        if new_files:
            print("New files detected:", new_files)
            for file in new_files:
                source_file = os.path.join(directory, file)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename, extension = os.path.splitext(file)
                new_filename = f"{filename}_{timestamp}{extension}"
                destination_file = os.path.join(destination_directory, new_filename)
                shutil.copy(source_file, destination_file)
                print(f"File '{file}' copied to '{destination_file}'")

        # Check for deleted files
        deleted_files = [file for file in previous_state if file not in current_state]
        if deleted_files:
            print("Deleted files detected:", deleted_files)

        # Update previous_state
        previous_state = current_state

if __name__ == "__main__":
    directory_to_monitor = "C:/Users/bulelani.kafu/Documents/"
    destination_directory = "C:/Users/bulelani.kafu/NewDocuments/"
    monitor_and_copy(directory_to_monitor, destination_directory)