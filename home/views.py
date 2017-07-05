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
    return render(request,"home.html",)