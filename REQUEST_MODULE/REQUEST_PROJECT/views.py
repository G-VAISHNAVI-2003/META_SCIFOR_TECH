from django.shortcuts import render
import requests

def get_posts(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    return render(request, 'REQ/reqmod/Template/posts.html', {'posts': posts})
