from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

#home url to drag and drop images to create custome minecraft paintings
def home(request):
    return render(request, 'minecraftpaintings/home.html')