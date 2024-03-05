from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def myview(request):
    return HttpResponse("<h1 style='color:yellow;background-color:blue;text-align:center'>hello world!,You are at the polls Index</h1>")
