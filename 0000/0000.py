from PIL import Image,ImageDraw,ImageFont

def addNum(filePath):
    img = Image.open(filePath)
    x, y = img.size
    fontSize = y / 4

    draw = ImageDraw.Draw(img)
    
    ttFont = ImageFont.truetype("/Library/Fonts/arial.ttf", fontSize)
    draw.text((size[0]-fontSize, 0), "6",(256,0,0), font=ttFont)
    del draw
    img.save('./result.jpg')
    img.show()


if __name__ == '__main__':
    addNum("dola.jpg")
