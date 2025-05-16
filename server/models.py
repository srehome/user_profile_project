from pydantic import BaseModel, Field, EmailStr, FilePath, field_validator
from typing import Optional, Annotated
from datetime import datetime
from werkzeug.security import generate_password_hash

class UserModel(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    birthday: datetime
    favorite_number: int
    profile_picture: Optional[FilePath] = None

    @field_validator("password", mode="before")
    def hash_password(cls, value):
        return generate_password_hash(value)
