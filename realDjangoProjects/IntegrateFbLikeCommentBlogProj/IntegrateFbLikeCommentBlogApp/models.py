from django.db import models
from django.contrib.auth.models import User #importing th user model here
from taggit.managers import TaggableManager
# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published_date=models.DateTimeField(auto_now_add=True)
    blog_img=models.ImageField(upload_to="media", blank=True, null=True)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    tags=TaggableManager()


    def __str__(self):
        return self.title

