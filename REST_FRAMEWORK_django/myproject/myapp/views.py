from django.shortcuts import render

# Create your views here.
import requests
from rest_framework import status,views
from rest_framework.response import Response
from .serializers import PostSerializer

def post_list_view(request):
        return render(request,'post_list.html')

class PostView(views.APIView):
    def get(self,request,pk=None):
        if pk:
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        else:
            response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return Response(response.json(),status=response.status_code)
    
    def post(self,request):
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            response = requests.post(f'https://jsonplaceholder.typicode.com/posts/{pk}',data=serializer.data)
            return Response(response.json(),status=response.status_code)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            response = requests.post(f'https://jsonplaceholder.typicode.com/posts/{pk}',data=serializer.data)
            return Response(response.json(),status=response.status_code)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{pk}',data=serializer.data)
            return Response(response.json(),status=response.status_code)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        return Response(status=response.status_code)

    def post_list_view(request):
        return render(request,'post_list.html')