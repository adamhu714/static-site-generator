import os
import shutil

def copy_static_dir():
    if not os.path.exists("./static/"):
        raise FileNotFoundError("static folder not found")
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")
    copy_recursion("./static/", "./public/", os.listdir("./static/"))

def copy_recursion(from_path, target_path, contents):
    for content in contents:
        if os.path.isdir(from_path + content):
            os.mkdir(target_path + content)
            copy_recursion(from_path + content + "/", target_path + content + "/", os.listdir(from_path + content))
        if os.path.isfile(from_path + content):
            shutil.copy(from_path + content, target_path + content)