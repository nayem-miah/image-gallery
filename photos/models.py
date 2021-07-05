from django.db import models

class Catagory(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Photo(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=300)
    photo = models.ImageField(null=False, blank=False)
    def __str__(self):
        return self.description