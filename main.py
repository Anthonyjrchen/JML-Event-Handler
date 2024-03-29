from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request
    })