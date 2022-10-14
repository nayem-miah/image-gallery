from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=10) 
    new_image = File(im_io, name=image.name)
    return new_image

class Catagory(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Photo(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=320)
    photo = models.ImageField(null=False, blank=False)
    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
                new_image = compress(self.photo)
                self.photo = new_image
                super().save(*args, **kwargs)




