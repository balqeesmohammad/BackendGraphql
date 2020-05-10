from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=50)

class Album(models.Model):
	albumname = models.CharField(max_length=50)
	artist =models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

class Song(models.Model):
	songtitle = models.CharField(max_length=50)
	album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)