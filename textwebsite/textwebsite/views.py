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
    djangotext = request.GET.get("text", "default")
    removingpunc = request.GET.get("removingpunc", "off")
    fullcaps = request.GET.get("fullcaps", "off")
    newlineremover=request.GET.get("newlineremover", "off")
    thespaceremover=request.GET.get("thespaceremover", "off")


#check the which check box is on
    if removingpunc == "on":
        punctuations = """!(){}[],.:;'"\/<>?#$%^&*_-"""
        analyzed = ""

        for char in djangotext:
            if char not in punctuations:
                analyzed += char

        # Return AFTER the loop
        params = {
            "purpose": "remove the punctuations",
            "analyzed_text": analyzed
        }
        return render(request, "analyze.html", params)
    elif fullcaps=="on":
        analyzed=""
        for char in djangotext:
            analyzed+=char.upper()
        params = {
            "purpose": "capitalized the text",
            "analyzed_text": analyzed
        }
        return render(request, "analyze.html", params)
    elif newlineremover=="on":
        analyzed = ""
        for char in djangotext:
            if char!= "\n":
                analyzed += char
        params = {
            "purpose": "removing the new line",
            "analyzed_text": analyzed
        }
        return render(request, "analyze.html", params)
    elif thespaceremover=="on":
        analyzed = ""
        for char in djangotext:
            if char !="  ":
                analyzed += char
        params = {
            "purpose": "removing the space from the text",
            "analyzed_text": analyzed
        }
        return render(request, "analyze.html", params)

    else:
        return HttpResponse("error")











# def capitalzingfirst (request):
#     return HttpResponse("hiusbdjk")
# def newlineremover (request):
#     return HttpResponse("newline remove")
# def thespaceremover (request):
#     return HttpResponse("remove the space<a href='/'> back</a>")
# def charactercount (request):
#     return HttpResponse("count the character")
