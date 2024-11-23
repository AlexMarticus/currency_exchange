from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int = Field(..., description="User's ID")
    email: EmailStr = Field(..., description="User's email")


class UserFromDB(User):
    password: str = Field(..., min_length=1, description="User's hashed password")
    password_salt: str = Field(..., description="User's uniq salt for password")