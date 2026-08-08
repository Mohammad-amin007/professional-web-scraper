from dataclasses import dataclass


@dataclass(slots=True)
class Book:
    title: str
    price: float
    availability: str
    rating: int
    product_url: str