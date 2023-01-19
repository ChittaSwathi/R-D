################################### Image difference with image URL starts ########################################

from PIL import Image
import requests,io

image_bytes = io.BytesIO(requests.get("IMAGE_PATH").content)

image_bytes1 = io.BytesIO(requests.get("IMAGE_PATH").content)

i1 = Image.open(image_bytes)
i2 = Image.open(image_bytes1)

assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."
 
pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)

################################### Image difference with image URL ends ########################################



################################### Image difference with image paths starts ######################################
from PIL import Image
 
i1 = Image.open("image1.jpg")
i2 = Image.open("image2.jpg")
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."
 
pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents) 

################################### Image difference with image paths ends ########################################
