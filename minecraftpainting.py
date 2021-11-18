# adding custom paintings into minecraft
from PIL import Image

size = 128

# copies image into kzpng
def copyImage(newImage, masterPng, startX, startY, multiplierX, multiplierY):
    newImage = newImage.convert('RGBA')
    for x in range(0, size * multiplierX):
      for y in range(0, size * multiplierY):
         r,g,b,a = newImage.getpixel((x,y))
         masterPng.putpixel((startX + x,startY + y), (r,g,b,a))
    #return masterPng




#Open original png size = (2048,2048)
ogImg = Image.open('image-collage/kz.png')



#change the first 7 images 0,1,2,3,4,5,6
for i in range(0,7):
    picName = 'images/' + str(i) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((size, size), Image.ANTIALIAS)
        copyImage(pImage, ogImg, size*i, 0, 1, 1)
    except:
        print(picName + ' not found')

#change the first 7 images 7,8,9,10,11
for i in range(0,5):
    picName = 'images/' + str(i+7) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize(((size*2), size), Image.ANTIALIAS)
        copyImage(pImage, ogImg, (size*2)*i, size*2, 2, 1)
    except:
        print(picName + ' not found')

#change the next 2 images 12, 13
for i in range(0,2):
    picName = 'images/' + str(i+12) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize((size, (size*2)), Image.ANTIALIAS)
        copyImage(pImage, ogImg, size*i, size*4, 1, 2)
    except:
        print(picName + ' not found')


#next image 14
picName = 'images/' + str(14) + '.png'
try:
    pImage = Image.open(picName)
    pImage = pImage.resize(((size*4), (size*2)), Image.ANTIALIAS)
    copyImage(pImage, ogImg, 0, size*6, 4, 2)
except:
    print(picName + ' not found')


#change the next 6 images 15, 16, 17, 18, 19, 20
for i in range(0,6):
    picName = 'images/' + str(i+15) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize(((size*2), (size*2)), Image.ANTIALIAS)
        copyImage(pImage, ogImg, (size*2)*i, size*8, 2, 2)
    except:
        print(picName + ' not found')

#change the next 3 images 21, 22, 23
for i in range(0,3):
    picName = 'images/' + str(i+21) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize(((size*4),(size*4)), Image.ANTIALIAS)
        copyImage(pImage, ogImg,(size*4)*i, size*12, 4, 4)
    except:
        print(picName + ' not found')


#next image
picName = 'images/' + str(24) + '.png'
try:
    pImage = Image.open(picName)
    pImage = pImage.resize(((size*4),(size*4)), Image.ANTIALIAS)
    copyImage(pImage, ogImg, size*12, 0, 4, 4)
except:
    print(picName + ' not found')




#change the last 2 images
for i in range(0,2):
    picName = 'images/' + str(i+25) + '.png'
    try:
        pImage = Image.open(picName)
        pImage = pImage.resize(((size*4), (size*3)), Image.ANTIALIAS)
        copyImage(pImage, ogImg, size*12,(size*4)+((size*3)*i), 4, 3)
    except:
        print(picName + ' not found')

ogImg.save('kz.png')

