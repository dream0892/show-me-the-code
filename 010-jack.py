from PIL import Image,ImageDraw,ImageFont
import pdb
import random,string
#打印验证码
KEY_LEN=4
def base_str():
    return (string.ascii_letters + string.digits)


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))
def random_color():
    rm_color=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    return rm_color



im=Image.new('RGB',(200,100),random_color())
font = ImageFont.truetype("arial.ttf", 40)
draw=ImageDraw.Draw(im)
for width in range(im.width):
    for height in range(im.height):
        if 80<random.randint(0,100):
            draw.point((width,height),fill=random_color())
strs=key_gen()
fw,fh=font.getsize(strs)
str_len=len(strs)
x=20
y=(im.height-fh)/2
for i in strs:  
    draw.text((x,y),i,font=font,fill=random_color())
    x=x+(im.width-40)/str_len
#pdb.set_trace()
im.show()