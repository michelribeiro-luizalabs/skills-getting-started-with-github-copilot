import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy

@pytest.fixture
def client():
    # Arrange: cria um TestClient para a aplicação
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: faz backup e restaura o banco de dados em memória antes de cada teste
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
