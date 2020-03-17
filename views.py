from django.http import HttpResponse
from django.shortcuts import render
import re
def index(request):
     return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover  = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':"Removed Punctuations",'analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': "Changed to upper case", 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = re.sub(' +',' ',djtext)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount == "on":
        count = len(djtext)-djtext.count(" ")
        params = {'purpose': "Character Count", 'analyzed_text': "{}\nCharacter Count:{}".format(djtext,count)}


    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount !="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
