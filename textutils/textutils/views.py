# I have creaated this file

from django.http import HttpResponse
from django.shortcuts import render






def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
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