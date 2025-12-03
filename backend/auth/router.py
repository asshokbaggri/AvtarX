from fastapi import APIRouter
from .signup import signup_user
from .login import login_user
from .verify import verify_token

router = APIRouter(tags=["Auth"])

@router.post("/signup")
def signup(data: dict):
    return signup_user(data)

@router.post("/login")
def login(data: dict):
    return login_user(data)

@router.post("/verify")
def verify(data: dict):
    return verify_token(data)
