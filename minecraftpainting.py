# adding custom paintings into minecraft
from PIL import Image

# copies image into kzpng
def copyImage(newImage, masterPng, startX, startY, multiplierX, multiplierY):
    newImage = newImage.convert('RGBA')
    for x in range(0, 16 * multiplierX):
      for y in range(0, 16 * multiplierY):
         r,g,b,a = newImage.getpixel((x,y))
         masterPng.putpixel((startX + x,startY + y), (r,g,b,a))
    #return masterPng




#Open original png size = (256,256)
ogImg = Image.open('kz.png')

#get first image #27 total
#pImages = [Image.open('1.png') for i in range(27)]




#change the first 7 images
for i in range(0,7):
    picName = str(i) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((16, 16), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 16*i, 0, 1, 1)
    except:
        print(picName + ' not found')

#change the first 7 images
for i in range(0,5):
    picName = str(i+7) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((32, 16), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 32*i, 16*2, 2, 1)
    except:
        print(picName + ' not found')

#change the next 2 images
for i in range(0,2):
    picName = str(i+12) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((16, 32), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 16*i, 16*4, 1, 2)
    except:
        print(picName + ' not found')

#next image
picName0 = str(14) + '.png'
try:
    pImage = Image.open(picName)
    pImage = pImage.resize((64, 32), Image.ANTIALIAS)
    copyImage(pImage, ogImg, 0, 16*6, 4, 2)
except:
    print(picName + ' not found')


#change the next 6 images
for i in range(0,6):
    picName = str(i+15) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((32, 32), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 32*i, 16*8, 2, 2)
    except:
        print(picName + ' not found')

#change the next 3 images
for i in range(0,3):
    picName = str(i+21) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((64, 64), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 64*i, 16*12, 4, 4)
    except:
        print(picName + ' not found')


#next image
picName = str(i+24) + '.png'
try:
    pImage = Image.open(picName)
    pImage = pImage.resize((64, 64), Image.ANTIALIAS)
    copyImage(pImage, ogImg, 16*12, 0, 4, 4)
except:
    print(picName + ' not found')




#change the last 2 images
for i in range(0,2):
    picName = str(i+25) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((64, 48), Image.ANTIALIAS)
        copyImage(pImage, ogImg, 16*12, 64+(48*i), 4, 3)
    except:
        print(picName + ' not found')

ogImg.save('kz1.png')

