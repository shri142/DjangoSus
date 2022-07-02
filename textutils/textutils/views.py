# I have creaated this file

from django.http import HttpResponse
from django.shortcuts import render






def index(request):
    return render(request,'index.html')
#
# def about(request):
#     return HttpResponse("hello in about")
#
# def joke(request):
#     file=open("fun.txt","r+")
#     data=file.read()
#     return HttpResponse(data)

# def index(request):
#     return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")