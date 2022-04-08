import sys
import os

from PIL import Image

path = sys.argv[1]
new_path = sys.argv[2]

if not os.path.exists(new_path):
    os.mkdir(new_path)

for files in os.listdir(path):
    img = Image.open(f'{path}{files}')
    rename = os.path.splitext(files)[0]
    img.save(f'{new_path}{rename}.png')
    print("Done")