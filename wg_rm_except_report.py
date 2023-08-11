import os
import shutil
import sys

def should_delete(file_name):
    return "report" not in file_name

def remove_folder_except_report(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if should_delete(file):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                remove_folder_except_report(dir_path)
        print("Files in '{}' deleted except 'report' files.".format(folder_path))
    except Exception as e:
        print("An error accurred: {}".format(e))
if len(sys.argv) != 2:
    print("Usage error")
else :
    target_folder = sys.argv[1]
    remove_folder_except_report(target_folder)
