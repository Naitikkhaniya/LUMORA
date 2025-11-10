# backend/app/core/deps.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.token import verify_token
from fastapi.security import HTTPBearer

oauth2_scheme = HTTPBearer()

def get_current_user(token = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raw = token.credentials  # "Bearer <...>" already parsed by HTTPBearer
    user_id = verify_token(raw, credentials_exception)
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise credentials_exception
    return user
