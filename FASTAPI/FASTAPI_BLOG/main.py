from fastapi import FastAPI, HTTPException
from typing import List
from models import Bgpost

app = FastAPI()

posts = [
    Bgpost(id=1, title="The first post", content="Introduction to python"),
    Bgpost(id=2, title="The second post", content="Class and objects concepts in python"),
    Bgpost(id=3, title="The third post", content="Understanding decorators in python"),
    Bgpost(id=4, title="The fourth post", content="Introduction to FastAPI"),
    Bgpost(id=5, title="The fifth post", content="Building REST APIs with FastAPI"),
    Bgpost(id=6, title="The sixth post", content="Async programming in python"),
    Bgpost(id=7, title="The seventh post", content="Introduction to SQLAlchemy"),
    Bgpost(id=8, title="The eighth post", content="Database migrations with Alembic"),
    Bgpost(id=9, title="The ninth post", content="Testing FastAPI applications"),
    Bgpost(id=10, title="The tenth post", content="Deploying FastAPI applications")
]

@app.get("/")
def read_root():
    return {"message": "Welcome to my blog.."}

@app.get("/posts", response_model=List[Bgpost])
def get_posts():
    return posts

@app.get("/posts/{post_id}", response_model=Bgpost)
def get_post(post_id: int):
    post = next((post for post in posts if post.id == post_id), None)
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts", response_model=Bgpost)
def create_post(post: Bgpost):
    posts.append(post)
    return post

@app.put("/posts/{post_id}", response_model=Bgpost)
def update_post(post_id: int, updated_post: Bgpost):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    global posts
    initial_length = len(posts)
    posts = [post for post in posts if post.id != post_id]
    if len(posts) < initial_length:
        return {"message": "Post deleted"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
