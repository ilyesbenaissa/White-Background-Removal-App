from PIL import Image
from PIL import ImageChops
import os
#make script as class to call it from gui_app.py

class RemoveBackground:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(self.filename)
        self.image = self.image.convert("RGBA")
        self.data = self.image.getdata()
        self.new_data = []
        
        for item in self.data:
            if is_white(item[0], item[1], item[2], item[3]) == 255:
                self.new_data.append((255, 255, 255, 0))
            else:
                self.new_data.append(item)
        self.image.putdata(self.new_data)
        self.image.save(os.path.splitext(self.filename)[0] + "_no_bg.png", "PNG")
        
def is_white(r, g, b, a):
    # if the pixel is close to white, make it transparent
    if r > 200 and g > 200 and b > 200:
        return 255
    # if the pixel is not close to white, keep it
    else:
        return 0        

'''
im= Image.open("C:\\Users\\ilyes\\Desktop\\test.png")

# make transparent png from image
im = im.convert("RGBA")
data = im.getdata()
# define a function to find all pixels that are close to white in a given image
def is_white(r, g, b, a):
    # if the pixel is close to white, make it transparent
    if r > 180 and g > 180 and b > 180:
        return 255
    # if the pixel is not close to white, keep it
    else:
        return 0

# apply the function to all pixels in the image
new_data = []
for item in data:
    if is_white(*item):
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

# create a new image with the new data
im.putdata(new_data)
#save to a new png file adding new number to the name each time
i = 0
while os.path.exists("C:\\Users\\ilyes\\Desktop\\test" + str(i) + ".png"):
    i += 1
im.save("C:\\Users\\ilyes\\Desktop\\test" + str(i) + ".png")

#find the word "Signature" in image and locate it
'''