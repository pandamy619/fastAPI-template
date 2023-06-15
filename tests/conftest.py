import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

