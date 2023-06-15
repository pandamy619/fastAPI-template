from typing import Dict
from fastapi import (
    APIRouter, 
    HTTPException, 
    status,
)

from fastapi_template.auth.schemas import (
    LoginSchemas,
    LoginResponseSchemas,
)
from fastapi_template.auth.service import (
    authenticate_user_service,
    get_user_from_email,
)


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/login",
    response_model=LoginResponseSchemas,
    responses={
        401: {
            "description": "Incorrect username or password",
            "content": {
                "application/json": {
                    "example": {"detail": "Incorrect username or password"}
                }
            },
        }
    }
)
async def login(params: LoginSchemas) -> Dict[str, str]:
    auth_status = authenticate_user_service(
        email=params.email, password=params.password
    )
    if not auth_status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    user = get_user_from_email(email=params.email)
    fake_token = "f+wvi5s2l%y$eht5oabkr))(hd=q*a^@#((!m%7*4e)v#m#kok"
    return LoginResponseSchemas(
        login=user["username"],
        token=fake_token
    )
