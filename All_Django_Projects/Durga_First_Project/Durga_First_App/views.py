from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(req):
    s="""<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./Bootstrap/css/bootstrap.css">
    <link rel="stylesheet" href="./Bootstrap/css/mdb.css">
</head>
<body>
<div class="container">
<h1 class="text-center">Welcome to django </h1>
<p class="lead">Read it Everyday to get habituated</p>
</div>
</body>
</html>"""

    return HttpResponse(s)
