from typing import Union
from fastapi import FastAPI, status, Response
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return authUsers()

@app.get("/authUsers/{internalId}")
def read_item(internalId : str):
    list=authUsers()
    for item in list:
        if item["internalId"]==internalId:
            return item
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)

def authUsers():
    url='https://630264749eb72a839d6ef2ff.mockapi.io/authUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()