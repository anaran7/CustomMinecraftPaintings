from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .forms import *


#home url to drag and drop images to create custome minecraft paintings
def home(request):
    if request.method == 'POST':
        form = PaintingsForm(request.POST, request.FILES)
  
        if form.is_valid():
            image = form.save(commit=False)
            image.painting_Name = str(request.POST['post_id'])
            image.save()
            
    else:
        form = PaintingsForm()
    return render(request, 'minecraftpaintings/home.html', {'form': form})


def update_collage(post_id):
    return 0