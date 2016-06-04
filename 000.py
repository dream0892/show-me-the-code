
from PIL import Image, ImageDraw ,ImageFont

im = Image.open("lena.pgm")
myfont=ImageFont.truetype('OpenSans-Light.ttf',size=40)
draw = ImageDraw.Draw(im)
draw.text((im.size[1]-40,0),'9',font=myfont,fill='#ff0000')
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)

del draw

# write to stdout
im.save('aaa', "PNG")


