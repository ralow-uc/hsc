from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_supersecreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 14

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)