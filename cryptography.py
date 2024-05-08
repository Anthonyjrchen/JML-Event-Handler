from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT


'''
PASSWORD HASHING
'''
SECRET_KEY = "a969379d6774b629d92dc6118ccb4c35f2676e5c3152bff4c9fbfb1bbff1bc0c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Use CryptContext to see if plain password matches hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)




'''
JWT_AUTH
'''
class Settings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_samesite: str = 'lax'

@AuthJWT.load_config
def get_config():
    return Settings()


