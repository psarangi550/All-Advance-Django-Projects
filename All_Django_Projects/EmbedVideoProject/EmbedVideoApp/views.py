from django.shortcuts import render
from .models import Video
# Create your views here.

def index_view(request):
    video_list=Video.objects.all()
    return render(request, "EmbedVideoApp/video.html", {"videos":video_list})
