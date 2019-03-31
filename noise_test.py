from PIL import Image
import time
import random
import glob, os

def save_image(image, path):
    im_name = str(time.time()*1000.0)
    path_name = str(path)
    new_name_with_path = path_name + im_name + ".jpg"
    image.save(path_name + "/" + im_name, 'JPEG')

print("something")

for filename in os.listdir('/home/jamie/Desktop/noise/originals'):
    curr_path = '/home/jamie/Desktop/noise/originals'
    im = Image.open(curr_path + "/" + filename)
    #new = Image.new("new", im.size, 0xffffff)
    w, h = im.size
    print("starting a range")
    new_im = Image.new("RGB", (w, h), "blue")
    pixels = new_im.load()
    for i in range(w):
        for j in range(h):
            these_pixels = list(im.getpixel((i, j)))
            #print("Original:")
            #print(these_pixels)
            these_pixels[0] = min(255, int(these_pixels[0]) + int(random.random()*100-50))
            #print("it worked?:")
            
            these_pixels[1] = min(255, int(these_pixels[1]) + int(random.random()*100-50))
            these_pixels[2] = min(255, int(these_pixels[2]) + int(random.random()*100-50))
            #print("NEW:")
            #print(these_pixels)
            

            pixels[i, j] = (these_pixels[0], these_pixels[1], these_pixels[2])
            #print("COPY")
            #print(pixels[i, j])

    save_image(new_im, '/home/jamie/Desktop/noise/with_noise')
    print("I randomized a file")

    print("got through a range")
