from PIL import Image
import time
import random
import glob, os

#/home/mypaintings/original
#/home/mypaintings/resize
#/home/mypaintings/rotated
#/home/mypaintings/flipped
#/home/mypaintings/randomized

size_sq = 64

print(random.randint(1,3))

def resize_image(image):
    size = size_sq, size_sq
##    return im.thumbnail(size)
    return image.resize(size, Image.NEAREST)

def rotate_image(image, path):
    im_1 = image.rotate(90)
    save_image(im_1, path)
    im_2 = image.rotate(180)
    save_image(im_2, path)
    im_3 = image.rotate(270)
    save_image(im_3, path)
    
def flip_image(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def save_image(image, path):
    im_name = str(time.time()*1000.0)
    path_name = str(path)
    new_name_with_path = path_name + im_name + ".jpg"
    image.save(path_name + "/" + im_name, 'JPEG')
    
    
for filename in os.listdir('/home/jamie/Desktop/mypaintings/originals'):
    curr_path = '/home/jamie/Desktop/mypaintings/originals'
    im = Image.open(curr_path + "/" + filename)
    small_img = resize_image(im)
    save_image(small_img, '/home/jamie/Desktop/mypaintings/resize')
    save_image(small_img, '/home/jamie/Desktop/mypaintings/rotated')
    rotate_image(small_img, '/home/jamie/Desktop/mypaintings/rotated')
    time.sleep(.1)

for filename in os.listdir('/home/jamie/Desktop/mypaintings/rotated'):
    curr_path = '/home/jamie/Desktop/mypaintings/rotated'
    im = Image.open(curr_path + "/" + filename)
    save_image(im, '/home/jamie/Desktop/mypaintings/flipped')
    new = flip_image(im)
    save_image(new, '/home/jamie/Desktop/mypaintings/flipped')
    time.sleep(.2)

##for lolz in range(3): 
    for filename in os.listdir('/home/jamie/Desktop/mypaintings/flipped'):
        curr_path = '/home/jamie/Desktop/mypaintings/flipped'
        im = Image.open(curr_path + "/" + filename)
        #new = Image.new("new", im.size, 0xffffff)
        w, h = im.size
        print("starting a range")
        for i in range(w):
            for j in range(h):
                these_pixels = list(im.getpixel((i, j)))
                print("Original:")
                print(these_pixels)
                these_pixels[0] = int(these_pixels[0]) + random.randint(0, 10) #(0, 1)*100-50
                #print("it worked?:")
                
                these_pixels[1] = int(these_pixels[1]) + random.randint(0, 10) #(0, 1)*100-50
                these_pixels[2] = int(these_pixels[2]) + random.randint(0, 10)  #(0, 1)*100-50
                print("NEW:")
                print(these_pixels)
                
                new_im = Image.new("RGB", (size_sq, size_sq), "black")
                pixels = new_im.load()
                pixels[i, j] = (these_pixels[0], these_pixels[1], these_pixels[2])
                print("COPY")
                print(pixels[i, j])

        save_image(new_im, '/home/jamie/Desktop/mypaintings/randomized')
        print("I randomized a file")

        print("got through a range")

            
                
        
        
    
    
