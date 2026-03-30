from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    # ... - означает, что поле должно быть обязательно заполнено
    name: str = Field(..., min_length=5, max_length=100,
                           description="Category name")
    slug: str = Field(..., min_length=5, max_length=100,
                           description="URL-friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category identifier')

    class Config:
        # позволяет создавать схему напрямую из модели
        form_attributes = True