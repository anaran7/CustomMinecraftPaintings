from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):
    '''
    overwrite files if they have the same name
    '''
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

def new_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.painting_Name, ext)
    return os.path.join('images', filename)

# Create your models here.
class Paintings(models.Model):
    painting_Name = 'default.png'
    painting_Img = models.ImageField(upload_to=new_file_name, storage=OverwriteStorage())
    

    def save(self, *args, **kwargs):
        self.name = self.painting_Name
        super(Paintings, self).save(*args, **kwargs)
    