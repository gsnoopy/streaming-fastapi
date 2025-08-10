from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base
from app.deps import get_db
from app.config import settings

TEST_DATABASE_URL = settings.test_database_url

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    db = TestingSessionLocal()
    try:
        from app.models.category import Category
        db.query(Category).delete()
        db.commit()
    finally:
        db.close()

# [TESTE PARA LISTAGEM DE CATEGORIAS VAZIAS]
def test_read_empty_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# [TESTE PARA CRIAÇÃO DE CATEGORIA VÁLIDA]
def test_create_category():
    response = client.post(
        "/categories/",
        json={"name": "Ação"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ação"
    assert "id" in data

# [TESTE PARA VALIDAÇÃO DE NOME MUITO PEQUENO]
def test_create_category_validation_error():
    response = client.post(
        "/categories/",
        json={"name": "ABC"} 
    )
    assert response.status_code == 422 

# [TESTE PARA CRIAÇÃO SEM NOME]
def test_create_category_missing_name():
    response = client.post(
        "/categories/",
        json={}
    )
    assert response.status_code == 422

# [TESTE PARA BUSCA DE CATEGORIA INEXISTENTE]
def test_read_category_not_found():
    response = client.get("/categories/9999")
    assert response.status_code == 404

# [TESTE PARA PAGINAÇÃO DE CATEGORIAS]
def test_read_category_pagination():
    response = client.get("/categories/?skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
