from PIL import Image
import numpy as np
import os
import shutil


dir = "/home/winter/code-resources/lighting/light-seg-sample/seg_labels"
names = [os.path.join(dir, n) for n in os.listdir(dir)]
total = len(names)
copied = 0
for n in names:
    img = Image.open(n)
    arr = np.array(img)
    mean = np.mean(arr)
    print(f"{n}, mean: {mean}")
    if (mean>0):
        shutil.copy(n, n.replace('labels','labels_pos'))
        copied += 1

print(f"total: {total}, copied: {copied}")