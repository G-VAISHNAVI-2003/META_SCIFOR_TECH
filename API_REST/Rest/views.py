from django.shortcuts import render
import requests

def fetch_posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    context = {'posts': posts}
    return render(request, 'posts.html', context)
