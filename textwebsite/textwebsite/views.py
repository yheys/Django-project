# i created this file
from email.policy import default

from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    pars={"name":"yheys","place": "addis ababa"}
    return render(request,"index.html", pars)

def about (request):
    return HttpResponse("<h1>yheys</h1>"  "<h2>yheys</h2>" )
def analyze(request):
    djangotext=request.GET.get("text","default")
    removingpunc = request.GET.get("remocingpunc", "off")
    print(removingpunc)
    print(djangotext)
    if removingpunc=="on":
        #analyzed=djangotext
        punctuations="""!(){}[],.:;'"\/<>?#$%^&*_-"""
        analyzed= ""
        for char in djangotext:
            if char not in punctuations:
                analyzed+=char

        params={"purpose": "remove the punctuations","analyzed_text": analyzed}
        return render(request,"analyze.html",params)
    # else:
    #     return HttpResponse("error")










# def capitalzingfirst (request):
#     return HttpResponse("hiusbdjk")
# def newlineremover (request):
#     return HttpResponse("newline remove")
# def thespaceremover (request):
#     return HttpResponse("remove the space<a href='/'> back</a>")
# def charactercount (request):
#     return HttpResponse("count the character")
