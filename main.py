from typing import Union
from fastapi import FastAPI, status, Response
from fastapi import FastAPI
import requests
import logging.config
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

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