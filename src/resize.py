import glob
import yaml
import os
import random
import sys
import shutil
from PIL import Image

params = yaml.safe_load(open("params.yaml"))["resize"]
if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

width = params["width"]
height = params["height"]

input_path = sys.argv[1]

def resize(input_path):
    dirs = glob.glob(input_path + "/*/*")
    renames = [i.replace("prepared","resized") for i in dirs]
    for i in renames:
        os.makedirs(i,exist_ok=True)
    images = glob.glob(input_path + "/*/**",recursive=True)
    images = [i for i in images if "jpeg" in i]
    for i in images:
        im = Image.open(i)
        im = im.resize((width,height))
        im = im.convert('RGB')
        im.save(i.replace("prepared","resized"))
    return True
print("INPUT",input_path)
print(resize(input_path))
