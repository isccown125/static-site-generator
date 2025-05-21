import os
import shutil



def clear_public_folder(target_folder):
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)
    os.makedirs(target_folder)

def copy_static_content(target_folder):
    static_folder = "static"
    for file in os.listdir(static_folder):
        if os.path.isfile(os.path.join(static_folder, file)):
            shutil.copy(os.path.join(static_folder, file), os.path.join(target_folder, file))
        elif os.path.isdir(os.path.join(static_folder, file)):
            shutil.copytree(os.path.join(static_folder, file), os.path.join(target_folder, file))







