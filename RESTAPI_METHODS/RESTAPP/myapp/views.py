from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


@api_view(['GET'])
def g_get(request):
    res = requests.get(BASE_URL)
    return Response(res.json(),status=res.status_code)

@api_view(['POST'])
def g_post(request):
    res = requests.post(BASE_URL,data = request.data)
    return Response(res.json(),status=res.status_code)

@api_view(['PUT'])
def g_put(request,post_id):
    url = f"{BASE_URL}/{post_id}"
    res = requests.put(url,data=request.data)
    return Response(res.json(),status=res.status_code)

@api_view(['PATCH'])
def g_patch(request,post_id):
    url = f"{BASE_URL}/{post_id}"
    res = requests.patch(url,data=request.data)
    return Response(res.json(),status=res.status_code)

@api_view(['DELETE'])
def g_delete(request,post_id):
    url = f"{BASE_URL}/{post_id}"
    res = requests.delete(url)
    return Response(res.json(),status=res.status_code)

