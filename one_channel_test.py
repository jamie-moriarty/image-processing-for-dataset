from PIL import Image
import time
import random
import glob, os

def save_image(image, path, filename):
    im_name = "new" + filename
    path_name = str(path)
    new_name_with_path = path_name + im_name + ".jpg"
    image.save(path_name + "/" + filename, 'JPEG')

for filename in os.listdir('/home/jamie/code/greyscale_test/converted'):
    curr_path = '/home/jamie/code/greyscale_test/converted'
    im = Image.open(curr_path+ "/" +filename)
    new_im = im.getchannel(0)
    save_image(new_im, '/home/jamie/code/greyscale_test/one_channel', filename)
    
