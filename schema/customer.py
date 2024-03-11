from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str

class CustomerCreate(BaseModel):
    username: str
    address: str


customers: list[Customer] = [
    Customer(id=1, username="omoyeni", address="11,oke aro str"),
    Customer(id=2, username="opeyemi", address="14, muri-okunola str")
]