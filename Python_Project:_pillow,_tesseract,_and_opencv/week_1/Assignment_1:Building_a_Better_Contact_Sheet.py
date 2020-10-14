#Arkanabytes

import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw,ImageFont
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
lables=[]
for i in range(3):
    for j in (0.1,0.5,0.9):
        source = image.split()
        lookup = source[i].point(lambda k:k*j)
        source[i].paste(lookup)
        getback = Image.merge(image.mode, source)
        lables.append('channel {} intensity {}'.format(i,j))
        images.append(getback)
txt_font = ImageFont.truetype("readonly/fanwood-webfont.ttf",75)

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+75*3))
x=0
y=0
draw_img=ImageDraw.Draw(contact_sheet)
for i,img in enumerate(images):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    draw_img.text((x,y+first_image.height+5), lables[i], font=txt_font)
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+75
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)



#############################
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont
#help(ImageDraw)
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
#Comes from PIL.ImageDraw-Gives us the text at the bottom of the image
def drawText(color, intensity,img):
text="channel {} intensity {}".format(color, intensity)
font = ImageFont.truetype(r'readonly/fanwood-webfont.ttf', 75)
Draw=ImageDraw.Draw(img)
Draw.text((10,470), text, font=font, align="left")
#Use the intensity and color to properly filter the picture
def imgFilter(brightness, img, color):
newImage = PIL.Image.new(img.mode, (newImg.width, newImg.height))
for row in range(height):
for col in range(width):
p = img.getpixel((col, row))
#Change the intensity for each color channel
#Images in row 1
if color == 0:
newImage.putpixel((col, row), (int(p[0]*brightness),p[1],p[2]))
#Images in row 2
elif color == 1:
newImage.putpixel((col, row), (p[0],int(p[1]*brightness),p[2]))
#Images in row 3
elif color == 2:
newImage.putpixel((col, row), (p[0],p[1],int(p[2]*brightness)))
return newImage
#The intensity and color options
intensity = [0.1, 0.5, 0.9]
colors = [0, 1, 2]
images=[]
#Use the two functions created to make the pictures and text
for color in colors:
for level in intensity:
images.append(imgFilter(level,newImg,color))
#This will draw the text on the last image appended
drawText(color, level, images[-1])
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.hei
ght*3))
x=0
y=0
for img in images:
# Lets paste the current image into the contact sheet
contact_sheet.paste(img, (x, y) )
# Now we update our X position. If it is going to be the width of the image, t
hen we set it to 0
# and update Y as well to point to the next "line" of the contact sheet.
if x+first_image.width == contact_sheet.width:

x=0
y=y+first_image.height
else:
x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_shee
t.height/2) ))
display(contact_sheet)
