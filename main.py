from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
import models
from models import User
from datetime import timedelta
import cryptography
import pandas as pd
import win32com.client as client


'''
FASTAPI SETUP
'''
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
outlook = client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")


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
    occupation: int
    first_name: str
    last_name: str

@app.post("/signup")
async def create_user(request: UserRequest, db : Session = Depends(get_db)):
    try:
        hashed_password = cryptography.get_password_hash(request.password)
        user = models.User(username=request.username, hashed_password=hashed_password, occupation=request.occupation, first_name = request.first_name, last_name = request.last_name)
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
    user = db.query(User).filter(User.username==username).first()
    return user

def authenticate_user(username: str, password: str, db):
    user = get_user(username, db)
    if not user:
        return False
    if not cryptography.verify_password(password, user.hashed_password):
        return False
    return user


@app.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), Authorize: AuthJWT = Depends(), db : Session = Depends(get_db)):    
    print("login function called")
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=cryptography.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = Authorize.create_access_token(subject=user.username, algorithm=cryptography.ALGORITHM ,expires_time=access_token_expires)
    refresh_token = Authorize.create_refresh_token(subject=user.username, algorithm=cryptography.ALGORITHM ,expires_time=access_token_expires)
    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return {"msg":"Login Successful"}

'''
LOG OUT
'''
@app.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    Authorize.unset_jwt_cookies()
    return {"msg": "Logout Successful"}


'''
SUPPORT TICKET ROUTE
'''
@app.post("/ticket/submit")
def support(request: Request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return request.headers["subject"] + " : " + request.headers["body"]


'''
GENERAL ROUTES
'''
@app.get("/")
def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html", {
        "request": request,
    })

@app.get("/home")
async def home(request: Request, Authorize: AuthJWT = Depends(), db : Session = Depends(get_db)):
    Authorize.jwt_required()
    calendars = []
    temp = []
    for idx, a in enumerate(namespace.getDefaultFolder(9).Folders):
        calendars.append(a.name)
    # for idx, a in namespace.getSharedDefaultFolder(9).Folders:
    #     temp.append(a.name)
    # return temp
    return templates.TemplateResponse("home.html", {
        "request": request,
        "page_location":"home",
        "calendars":calendars,
        "fn":get_user(Authorize.get_jwt_subject(), db).first_name,
    })

@app.get("/calendars")
def calendars(request: Request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return templates.TemplateResponse("calendars.html", {
        "request": request,
        "page_location":"calendars"
    })

@app.get("/settings")
def remove(request: Request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "page_location":"settings"
    })

@app.get("/support")
def support(request: Request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return templates.TemplateResponse("support.html", {
        "request": request,
        "page_location":"support"
    })