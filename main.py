from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests

from preprocess import preprocessing

app = FastAPI()

@app.post("/json")

async def get_body(request: Request):
    return await request.body()

@app.get("/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/")
def read_user(url: str):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    titles = soup.findAll('title')
    for data in titles:
        filtered_titles.append(data.text)
    return {"result": preprocessing(filtered_titles)}