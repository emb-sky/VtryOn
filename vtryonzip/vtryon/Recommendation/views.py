from django.shortcuts import render

import pandas as pd
import numpy as np
import joblib
import json
import os
import logging
# import pymongo
import warnings
import re
warnings.filterwarnings("ignore")
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from apyori import apriori

import requests
@api_view(['GET','POST'])
@csrf_exempt
def vtroom(request):
    try:
        

        api_url = "https://vtroom.embdev.in/rest/V1/getproducts?searchCriteria[pageSize]=10"
        api_key = "eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjQsInV0eXBpZCI6MiwiaWF0IjoxNzAxMDg4MjEyLCJleHAiOjE3MDEwOTE4MTJ9.B_b6h2Tg6JRPpB57jg7UPAApF2L3J5HOKm8sT-646p0"

        response = requests.get(api_url, headers={'Authorization': f'Bearer {api_key}'})


        data = response.json()
        showdata = pd.DataFrame(data)
        showdata=showdata['ItemName'][2]
        logging.info(f"Recommended products are: {showdata}")
        return JsonResponse({"status":"success","response_data":showdata})
    except Exception as e:
    
        return JsonResponse({'status': 'failure', 'response': f"An error occurred: {str(e)}"})