from django.shortcuts import render
from django.views.generic.base import RedirectView
# Create your views here.
class MyRedirectView(RedirectView):
    pattern_name="home"
    permanent=True
    id=""
    query_string=True
    def get_redirect_url(self,*args,**kwargs):
        global id
        id=self.kwargs["id"]
        my_string=kwargs["path"]
        my_new_string=kwargs["path"]
        print(my_new_string)
        return super().get_redirect_url(*args,**kwargs)
    # def get_context_data(self,*args,**kwargs):
    #     context=super().get_context_data(*args,**kwargs)
    #     context['id']=self.id
    #     return context




