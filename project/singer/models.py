from django.db import models

# Create your models here.

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    debut = models.CharField(max_length=50)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=50, default='Unknown')
    release = models.CharField(max_length=50)
    content = models.TextField(max_length=200)

