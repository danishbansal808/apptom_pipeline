import glob
import yaml
import os
import random
import sys
import shutil

params = yaml.safe_load(open("params.yaml"))["split"]
if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

# Test data set split ratio
split = params["percentage"]
random.seed(params["seed"])

input_path = sys.argv[1]
output_train = os.path.join("data", "prepared", "train")
output_test = os.path.join("data", "prepared", "test")

def split_datastet(input_path, output_train, output_test, split_perc):
    classes_paths = glob.glob(input_path+"/*")
    class_names = [i.split("/")[-1] for i in classes_paths]
    images = {}
    for i,j in zip(classes_paths,class_names):
        images[j] = glob.glob(i+"/*")
        random.shuffle(images[j])
    for i in class_names:
        data = images[i]
        n = int(len(data) * split_perc)
        train = data[:n]
        test = data[n:]
        os.makedirs(os.path.join(output_train,i),exist_ok=True)
        for img in train:
            shutil.copy(img,os.path.join(output_train,i))
        os.makedirs(os.path.join(output_test,i),exist_ok=True)
        for img in test:
            shutil.copy(img,os.path.join(output_test,i))
    return True
print("INPUT",input_path)
split_datastet(input_path, output_train, output_test, split)
