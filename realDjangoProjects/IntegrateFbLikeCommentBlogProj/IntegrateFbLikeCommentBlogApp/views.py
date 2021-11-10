from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import EmailSendForm
from django.conf import settings
from django.urls import reverse
# Createur views here.

#blog_list_view
def blog_list_view(request):
    blog_list=Blog.objects.all()
    paginator=Paginator(blog_list,3)
    page_number=request.GET.get("page")
    pages=paginator.get_page(page_number)
    context={"pages":pages}
    return render(request, "IntegrateFbLikeCommentBlogApp/blog_list.html", context)

#blog_detail view
def blog_detail_view(request,id):
    blog=get_object_or_404(Blog,id=id)
    context={"blog":blog}
    return render(request, "IntegrateFbLikeCommentBlogApp/blog_detail.html",context)

#Email Send Form functionality
def EmailSendView(request,id):
    blog=get_object_or_404(Blog,id=id)
    sent=False
    if request.method == "POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            to=form.cleaned_data["to"]
            sender=form.cleaned_data['name']
            comments=form.cleaned_data["comments"]
            url=str(request.build_absolute_uri(reverse("blog_detail",kwargs={"id":blog.id})))
            comment=f'{comments}\n\n{url}'
            subject=f'{sender}recomend you {blog.title}'
            send_mail(subject , comment , settings.EMAIL_HOST_USER , [to])
            sent=True
    else:
        form=EmailSendForm()
    return render(request, "IntegrateFbLikeCommentBlogApp/email_send.html", {"form":form,"blog":blog,"sent":sent})
