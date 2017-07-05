from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import os
import os.path
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

from polls.models import Document
from polls.forms import DocumentForm

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def index(request):
   

    if request.method=='POST':
        #print("TEST")
        #test = request.POST['filePath']
        #print(request.FILES)
        form = DocumentForm(request.POST, request.FILES)
        
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key='720d070883d98b59667185e9dec66d4e11dfc793')
        
        url = request.POST["url"]
        if not url:
            data = request.FILES["docfile"]
            path = default_storage.save('temp.jpg', ContentFile(data.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            print(tmp_file)
            with open((tmp_file), 'rb') as img:
                a = visual_recognition.classify(images_file=img)

        #print(test)
        #variable = str(test)
        #variable = "C://Users/Milan/fruitbowl.jpg"
        #variable = test
        else:
            a = visual_recognition.classify(images_url=url)
        

        
            
        print(a)
        #for i in range (0,3):
        #    print(a['images'][0]['classifiers'][0]['classes'][i]['class']+str(a['images'][0]['classifiers'][0]['classes'][i]['score'])+ "\n")
        print(a)
        
        html = ""
        for i in range(0,3):
         html += "<h1>"+a['images'][0]['classifiers'][0]['classes'][i]['class']+"-----"+str(a['images'][0]['classifiers'][0]['classes'][i]['score'])+"</h1>"
        html += "<img src='/Users/Milan/myproject/media/temp.jpg' height='100px'/>"   
    #username = request.post.get('username')

        #print("\n\n\n",test,"\n\n\n")

    #return HttpResponse(html)
        return render(request,"imgRes.html",{'res':json.dumps(a)})
    return render(request,"ibm3.html")
    

