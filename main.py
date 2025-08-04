'''
Main file for this project.
'''

from fastapi import FastAPI

app = FastAPI()

# Get the routes from api folder

# Define first route for this project
@app.get("/")
async def welcome_page() -> dict[str, int | str]:
  return {
    "status": 200,
    "message":"Welcome to the Auto Exploratory Data Analysis Project"
  }