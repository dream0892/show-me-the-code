#在图标左上角加上数字
from PIL import Image, ImageDraw ,ImageFont

im = Image.open("lena.pgm")
width,height=im.size
myfont=ImageFont.truetype('OpenSans-Light.ttf',size=int(height*0.2))
draw = ImageDraw.Draw(im)
draw.text((im.size[1]-height*0.2,0),'9',font=myfont,fill='#ff0000')
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw
im.save('aaa.png', "PNG")


