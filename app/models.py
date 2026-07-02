from pydantic import BaseModel


class SearchRequest(BaseModel):
    product: str
    max_price: int | None = None
    shop: str | None = None


class Product(BaseModel):
    title: str
    price: int
    shop: str
    url: str