import datetime
import uuid
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

class PostBase(BaseModel):
    """Base schema for a blog post."""
    title: str = Field(..., example="My First Blog Post")
    content: str = Field(..., example="This is the amazing content of my first post.")

class PostCreate(PostBase):
    """Schema for creating a new post."""
    pass

class PostUpdate(BaseModel):
    """Schema for updating an existing post (all fields are optional)."""
    title: Optional[str] = Field(None, example="Updated Post Title")
    content: Optional[str] = Field(None, example="The revised content for the post.")

class PostOut(PostBase):
    """Schema for the post returned by the API."""
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    author: str = Field(..., example="Admin User")
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


fake_db: dict[uuid.UUID, dict] = {}
CURRENT_AUTHOR = "FastAPI Dev"


app = FastAPI(
    title="Simple Blog CMS API",
    description="A basic CRUD API for managing blog posts using FastAPI.",
    version="1.0.0",
)

origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
    allow_headers=["*"],
)



@app.get("/", status_code=status.HTTP_200_OK, tags=["Root"])
def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Simple Blog CMS API. Use /docs for the API specification."}

@app.post("/posts/", response_model=PostOut, status_code=status.HTTP_201_CREATED, tags=["Posts"])
def create_post(post: PostCreate):
    """
    Creates a new blog post.
    """
    post_id = uuid.uuid4()
    now = datetime.datetime.now(datetime.timezone.utc)
    
    new_post = {
        "id": post_id,
        "title": post.title,
        "content": post.content,
        "author": CURRENT_AUTHOR,
        "created_at": now,
        "updated_at": now
    }
    
    fake_db[post_id] = new_post
    
    return new_post

@app.get("/posts/", response_model=List[PostOut], tags=["Posts"])
def read_all_posts():
    """
    Retrieves a list of all existing blog posts.
    """
    return list(fake_db.values())

@app.get("/posts/{post_id}", response_model=PostOut, tags=["Posts"])
def read_post(post_id: uuid.UUID):
    """
    Retrieves a single blog post by its unique ID.
    """
    if post_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID: {post_id} not found"
        )
    return fake_db[post_id]

@app.put("/posts/{post_id}", response_model=PostOut, tags=["Posts"])
def update_post(post_id: uuid.UUID, post_update: PostUpdate):
    """
    Updates an existing blog post. Only provided fields (title/content) are modified.
    """
    if post_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID: {post_id} not found"
        )

    existing_post = fake_db[post_id]
    
    update_data = post_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        existing_post[key] = value

    existing_post["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
    
    fake_db[post_id] = existing_post
    
    return existing_post

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Posts"])
def delete_post(post_id: uuid.UUID):
    """
    Deletes a blog post by its unique ID.
    """
    if post_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID: {post_id} not found"
        )
        
    del fake_db[post_id]
    
    return