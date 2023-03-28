'''
Written by Pablo Salazar Navalon
              28 March 2022

Here are all schemas used as response/request of the API functions
'''
from pydantic import BaseModel

class Product(BaseModel):
    brand: str
    type: str
    calories: int
    fatPerc: float
    sugarPerc: float

class Establishment(BaseModel):
    name: str
    address: str
    openingHours: str

class Price(BaseModel):
    productID: int
    establishmentID: int
    price: float