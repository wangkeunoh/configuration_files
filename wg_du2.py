import os 

def get_human_readable_size(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0;
    while size >= 1024 and index < len(units) -1 :
        size /= 1024
        index += 1
    return "{:.1f} {}".format(size, units[index])


def get_actual_file_size(path):
    if os.path.islink(path):
        return 0
    else:
        return os.path.getsize(path)

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += get_actual_file_size(file_path)
    return total_size

subfolders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]
sorted_subfolders = sorted(subfolders, key=lambda folder: get_folder_size(folder))

for i, folder in enumerate(sorted_subfolders, start=1):
  size = get_folder_size(folder)
  size_human_redable = get_human_readable_size(size)
  print("{0}. {1}, {2}".format(i, size_human_redable, folder))
  
