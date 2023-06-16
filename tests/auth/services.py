import pytest
from fastapi_template.fastapi_template.auth.services import get_user_from_email


@pytest.mark.parametrize(
    "email, expected_response",
    (("user1@email.com", None),),
)
def test_get_user_from_email(client, email, expected_response):
    user = get_user_from_email(email=email)
    assert user == expected_response
