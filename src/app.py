from fastapi import FastAPI, HTTPException
from src.schemas import PostCreate, PostResponse
from src.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI()

# handling posts

text_posts = {
    1: {
        "title": "Introduction to FastAPI",
        "content": "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints."
    },
    2: {
        "title": "Understanding Python Type Hints",
        "content": "Type hints (PEP 484) help you write more readable and maintainable code. They are central to how FastAPI validates data."
    },
    3: {
        "title": "Debugging with Uvicorn",
        "content": "Uvicorn is an ASGI server often used with FastAPI. The --reload flag is crucial for fast development cycles."
    },
    4: {
        "title": "The Power of Pydantic",
        "content": "Pydantic is a library that provides data validation and settings management using Python type annotations. It handles the JSON schema for FastAPI."
    },
    5: {
        "title": "Creating Path Parameters",
        "content": "Path parameters allow you to capture variable parts of a URL, which is essential for endpoints like /posts/{id}."
    },
    6: {
        "title": "Status Codes Explained",
        "content": "HTTP status codes (like 200, 404, 500) are vital for letting the client know the outcome of their request."
    },
    7: {
        "title": "Query Parameters vs. Path Parameters",
        "content": "Query parameters are used for optional filtering or pagination, while path parameters identify a specific resource."
    },
    8: {
        "title": "What is ASGI?",
        "content": "ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, designed to support asynchronous Python web apps."
    },
    9: {
        "title": "A Look at Asynchronous Python (async/await)",
        "content": "The async and await keywords enable concurrent operations, allowing your server to handle many requests simultaneously."
    },
    10: {
        "title": "Securing Your API",
        "content": "Authentication and authorization are crucial steps in API development, ensuring only legitimate users can access your data."
    }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post_by_id(id:int):
    if id not in text_posts:
        raise HTTPException(404, "Post not found")

    return text_posts[id]

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {
        "id": max(text_posts.keys()) + 1,
        "title": post.title,
        "content": post.content
    }

    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

# @app.delete()
