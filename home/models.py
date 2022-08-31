from turtle import title
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=125)
    phone=models.CharField(max_length=12)
    date=models.DateField()

class video(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']

class video_10(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']

class video_11ip(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']

class video_11cs(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']

class video_12ip(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']

class video_12cs(models.Model):
    title= models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) :
        return str(self.title)

    class Meta:
        ordering =['-added']