from dataclasses import dataclass


@dataclass(slots=True)
class Book:
    title: str
    price: float