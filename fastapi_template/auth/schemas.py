from pydantic import BaseModel


class LoginSchemas(BaseModel):
    email: str
    password: str


class LoginResponseSchemas(BaseModel):
    login: str
    token: str
