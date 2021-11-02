from django.db import models

# Create your models here.
class PostManage(models.Manager):
    def get_queryset(self,*args, **kwargs):
         post=super().get_queryset(*args, **kwargs)
         return post.order_by("created")
class PostManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
         post=super().get_queryset(*args, **kwargs)
         return post.order_by("-updated")

class Post(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    objects=models.Manager()
    custom=PostManage()


class PostProxy(Post):
    custom=PostManager()
    objects=models.Manager()
    class Meta:
        proxy=True


