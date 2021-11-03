
from django.shortcuts import render,HttpResponse

class MyMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response
    def __call__(self,request):
        resp=self.get_response(request)
        resp.context_data["name"]="Rika"
        return resp
    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     view_kwargs["name"]="pratik"
    # def process_exception(self,request,exception):
    #     return render(request, "RevesionMiddlewareApp/home.html")
    def process_template_response(self,request,response):
        response.context_data["msg"]="welcome"
        response.context_data["name"]="Rika"
        return response



