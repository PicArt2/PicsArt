import os
import os.path
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='720d070883d98b59667185e9dec66d4e11dfc793')

with open(os.path.join(os.path.dirname(__file__), 'C://Users/Anirudh/beagle.jpg'), 'rb') as img:
	print(json.dumps(visual_recognition.classify(images_file=img, threshold = 0.8), indent=2))
