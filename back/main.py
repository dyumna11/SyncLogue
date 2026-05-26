from database import collection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend working"}

@app.get("/github/{username}")
def github_user(username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    data = response.json()

    if data.get("message") == "Not Found":
        return data

    collection.insert_one({
        "username": data["login"],
        "repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"],
        "avatar": data["avatar_url"]
    })

    return data