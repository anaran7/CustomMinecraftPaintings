from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from PIL import Image
import mimetypes


#home url to drag and drop images to create custome minecraft paintings
def home(request):
    if request.method == 'GET' and  request.GET.get('post_id') == '100':
        resetImage()
        
    if request.method == 'POST':
        
        form = PaintingsForm(request.POST, request.FILES)
  
        if form.is_valid():
            image = form.save(commit=False)
            image.painting_Name = str(int(request.POST['post_id'])-1)
            image.save()
            update_collage(int(request.POST['post_id']))
            
    else:
        form = PaintingsForm()
    return render(request, 'minecraftpaintings/home.html', {'form': form})

def copyImage(newImage, masterPng, startX, startY, multiplierX, multiplierY, size=128):
    newImage = newImage.convert('RGBA')
    for x in range(0, size * multiplierX):
      for y in range(0, size * multiplierY):
         r,g,b,a = newImage.getpixel((x,y))
         masterPng.putpixel((startX + x,startY + y), (r,g,b,a))

def imageSetUp(picName, ogImg, post_id, a, b, c, d, e, f):
    try:
        picPNG = picName + '.png'
        pImage = Image.open(picPNG)
        pImage = pImage.resize((a, b), Image.ANTIALIAS)
        copyImage(pImage, ogImg, c, d, e, f)
    except:
        print(picPNG + ' not found')
        try:
            picJPG = picName + '.jpg'
            pImage = Image.open(picJPG)
            pImage = pImage.resize((a, b), Image.ANTIALIAS)
            copyImage(pImage, ogImg, c, d, e, f)
        except:
            print(picJPG + ' not found')
            try:
                picJPEG = picName + '.jpeg'
                pImage = Image.open(picJPEG)
                pImage = pImage.resize((a, b), Image.ANTIALIAS)
                copyImage(pImage, ogImg, c, d, e, f)
            except:
                print(picJPEG + ' not found')
    

def update_collage(post_id, size=128):
    ogImg = Image.open('minecraftpaintings/static/images/kz.png')
    post_id = post_id - 1
    picName = 'media/images/' + str(post_id)
    if post_id >= 0 and post_id < 7:
        imageSetUp(picName, ogImg, post_id, size, size, size*post_id, 0, 1, 1)
    elif post_id >= 7 and post_id < 12:
        post_id = post_id - 7
        imageSetUp(picName, ogImg, post_id, (size*2), size, (size*2)*post_id, size*2, 2, 1)
    elif post_id >= 12 and post_id < 14:
        post_id = post_id - 12
        imageSetUp(picName, ogImg, post_id, size, (size*2), size*post_id, size*4, 1, 2)
    elif post_id == 14:
        post_id = post_id - 14
        imageSetUp(picName, ogImg, post_id, (size*4), (size*2), 0, size*6, 4, 2)
    elif post_id >= 15 and post_id < 21:
        post_id = post_id - 15
        imageSetUp(picName, ogImg, post_id, (size*2), (size*2), (size*2)*post_id, size*8, 2, 2)
    elif post_id >= 21 and post_id < 24:
        post_id = post_id - 21
        imageSetUp(picName, ogImg, post_id, (size*4),(size*4), (size*4)*post_id, size*12, 4, 4)
    elif post_id == 24:
        post_id = post_id - 24
        imageSetUp(picName, ogImg, post_id, (size*4),(size*4), size*12, 0, 4, 4)
    elif post_id >= 25 and post_id < 27:
        post_id = post_id - 25
        imageSetUp(picName, ogImg, post_id, (size*4), (size*3), size*12,(size*4)+((size*3)*post_id), 4, 3)
    else:
        print(post_id)
        print("Image has incorrect name")
    
    ogImg.save('minecraftpaintings/static/images/kz.png')

def resetImage():
    ogImg = Image.open('minecraftpaintings/static/images/kz_og.png')
    newOG = ogImg.copy()
    newOG.save('minecraftpaintings/static/images/kz.png')

