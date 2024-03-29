from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory=r"C:\Users\antho\Desktop\JML Event Handler\static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html", {
        "request": request,
    })

@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "page_location":"home"
    })

@app.get("/remove")
def remove(request: Request):
    return templates.TemplateResponse("remove.html", {
        "request": request,
        "page_location":"remove"
    })

@app.get("/calendars")
def calendars(request: Request):
    return templates.TemplateResponse("calendars.html", {
        "request": request,
        "page_location":"calendars"
    })

@app.get("/calculator")
def calculators(request: Request):
    return templates.TemplateResponse("calculator.html", {
        "request": request,
        "page_location":"calculator"
    })