from PIL import Image
import time
import random
import glob, os

def save_image(image, path, filename):
    im_name = "new" + filename
    path_name = str(path)
    new_name_with_path = path_name + im_name + ".jpg"
    image.save(path_name + "/" + filename, 'JPEG')

for filename in os.listdir('/home/jamie/code/greyscale_test/color'):
    curr_path = '/home/jamie/code/greyscale_test/color'
    im = Image.open(curr_path+ "/" +filename).convert('L')
    save_image(im, '/home/jamie/code/greyscale_test/converted', filename)
    
