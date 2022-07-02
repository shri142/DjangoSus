# I have creaated this file

from django.http import HttpResponse
def index(request):
    return HttpResponse("hello")