from pydantic import BaseModel, Field


class MenuSchema(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class SubMenuSchema(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class DishesSchema(BaseModel):
    title: str
    description: str
    price: float = Field(dt=0)

    class Config:
        orm_mode = True
