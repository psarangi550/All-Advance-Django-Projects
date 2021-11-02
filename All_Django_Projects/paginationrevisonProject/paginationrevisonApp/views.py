from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.
def index_view(request):
    blog=Blog.objects.all()
    paginator=Paginator(blog,per_page=2,orphans=1)
    page_number=request.GET.get("mypage")
    pages=paginator.get_page(page_number)
    return render(request, "paginationpaginationrevisonApp/index.html" ,{"pages":pages})
