from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
import models
from models import User
import cryptography
import random
app = FastAPI()
app.mount("/static", StaticFiles(directory=r"C:\Users\antho\Desktop\JML Event Handler\static"), name="static")
templates = Jinja2Templates(directory="templates")

'''
DATABASE SETUP AND CONNECTION
'''
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
models.Base.metadata.create_all(bind=engine)

'''
JWT_AUTH EXCEPTION HANDLER
'''
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    if exc.message=="Signature has expired":
        return RedirectResponse("/")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

'''
USER SIGNUP
'''
class UserRequest(BaseModel):
    username: str
    password: str

@app.post("/signup")
async def create_user(request: UserRequest, db : Session = Depends(get_db)):
    try:
        hashed_password = cryptography.get_password_hash(request.password)
        user = models.User(username=request.username, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        return {"True"}
    except Exception as err:
        print(err)
        return {"False"}

@app.get("/signup")
def landing_page(request: Request):
    return templates.TemplateResponse("signup.html", {
        "request": request,
    })
    
'''
USER LOGIN
'''
def get_user(username: str, db):
    users = db.query(User).filter(User.username==username).first()
    return users

def authenticate_user(username: str, password: str, db):
    user = get_user(username, db)
    if not user:
        return False
    if not cryptography.verify_password(password, user.hashed_password):
        return False
    return user


'''
GENERAL ROUTES
'''
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