from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

class Video(models.Model):
    name=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    url=EmbedVideoField()

    def __str__(self):
        return self.name
