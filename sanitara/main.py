""" """

import re
import typing
import regex as regex

from fastapi import FastAPI
from processing import pipelines

app = FastAPI()

@app.get("/api/v1/predict/")
async def root(message: str):

    print(f"Received input message: {message}")
    return pipelines.predict(message)


