import base64
import requests
import shutil
import hashlib
import pickle
import os
import numpy as np
from PIL import Image


url = 'https://wallpaperaccess.com/full/3659953.jpg'
temporary_name = url.split('/')[-1]

r = requests.get(url, stream=True)

if r.status_code == 200:
    r.raw.decode_content = True
    with open(temporary_name, 'wb') as image_file:
        shutil.copyfileobj(r.raw, image_file)
        image_file.close()

    with open(temporary_name, 'rb') as image:
        encoded_image = base64.b64encode(image.read())
        image.close()

    with open('binary_file', 'wb') as b_file:
        pickle.dump(encoded_image, b_file)
        b_file.close()

    with open('binary_file', 'rb') as b_file:
        binary_file = pickle.load(b_file)
        md_file_name = f"{hashlib.md5(b_file.read()).hexdigest()}"
        os.rename('binary_file', md_file_name)
        b_file.close()

    with open(md_file_name, 'rb') as f:
        w = 50
        h = 100
        d = np.fromfile(f, dtype=np.uint8, count=w * h).reshape(h, w)
    PILimage = Image.fromarray(d)
    PILimage.save(f'{md_file_name}.jpg')
