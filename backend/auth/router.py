from fastapi import APIRouter
from .login import login_user
from .signup import signup_user
from .verify import verify_token

router = APIRouter()

@router.post("/signup")
def signup(data: dict):
    return signup_user(data)

@router.post("/login")
def login(data: dict):
    return login_user(data)

@router.post("/verify")
def verify(data: dict):
    return verify_token(data)
