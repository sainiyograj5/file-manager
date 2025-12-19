from pydantic import BaseModel, EmailStr
from datetime import datetime

class SignupRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FileResponse(BaseModel):
    id: int
    filename: str
    mime_type: str
    uploaded_at: datetime
    url: str

    class Config:
        from_attributes = True
