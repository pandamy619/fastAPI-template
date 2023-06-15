from typing import Optional, Dict, Any

MOCK_USER = {
    "user@email.com": {
        "id": 1,
        "username": "user",
        "email": "user@email.com",
        "role": "user"
    }
}


def get_user_from_email(email: str) -> Optional[Dict[str, Any]]:
    return MOCK_USER.get(email, None)


def authenticate_user_service(email: str, password: str) -> bool:
    db_user = get_user_from_email(email=email)
    if not db_user:
        return False
    return True

