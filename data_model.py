from pydantic import BaseModel

class DataModel(BaseModel):
    age: int
    balance: float
    country: str
    products_number: int
    active_member: int
