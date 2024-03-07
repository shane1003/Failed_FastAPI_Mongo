"""
create a base route
Tags are identifiers used to group routes.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"Message" : "Welcome to this fantastic app!"}