from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "page_location":"home"
    })

@app.get("/remove")
def home(request: Request):
    return templates.TemplateResponse("remove.html", {
        "request": request,
        "page_location":"remove"
    })

@app.get("/calendars")
def home(request: Request):
    return templates.TemplateResponse("calendars.html", {
        "request": request,
        "page_location":"calendars"
    })

@app.get("/calculator")
def home(request: Request):
    return templates.TemplateResponse("calculator.html", {
        "request": request,
        "page_location":"calculator"
    })