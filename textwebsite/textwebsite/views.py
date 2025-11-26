# i created this file

from django.http import HttpResponse
def index (request):
    return HttpResponse("hi yheys")

def about (request):
    return HttpResponse("<h1>yheys</h1>"  "<h2>yheys</h2>" )