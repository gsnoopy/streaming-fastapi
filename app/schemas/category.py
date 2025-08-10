from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=4, description="Nome da categoria deve ter pelo menos 4 caracteres")

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    model_config = dict(from_attributes=True)
