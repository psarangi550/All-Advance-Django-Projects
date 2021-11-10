from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
def index_view(request):
    # value={"name":"rika","roll":100}
    # cache.set_many(value,timeout=300,version=1)
    # stu_details=cache.get_many(value)
    # return render(request, "lowlevelcacheApiRevApp/index.html", stu_details)
    cache.clear()
    movies=cache.get("mv")
    if movies == None :
        cache.set("mv","lock undeneath")
        # movies=cache.get("movies")
    else:
        movies=cache.get("mv")
    return render(request, "lowlevelcacheApiRevApp/index.html", {"name":cache.get("mv")})


