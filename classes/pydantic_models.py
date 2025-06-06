# pydantic_examples.py

from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List

# ✅ Validation & 🔄 Type Coercion
class User(BaseModel):
    username: str
    email: EmailStr
    age: int  # Will coerce "30" (str) to 30 (int)

# 🧵 Nested Models
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Profile(BaseModel):
    user: User
    address: Address

# 🛠️ Custom Validation
class Product(BaseModel):
    name: str
    price: float

    @validator("price")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v

# 🔐 Optional / Default Fields
class Settings(BaseModel):
    debug: bool = False
    timeout: Optional[int] = None
    retries: int = 3

# 🌐 JSON Serialization
def demo_serialization():
    user = User(username="kevin", email="kevin@example.com", age="30")
    print("User (as dict):", user.dict())
    print("User (as JSON):", user.json())

    address = Address(street="123 Main St", city="Orlando", zip_code="32801")
    profile = Profile(user=user, address=address)
    print("Profile (nested model):", profile)

    product = Product(name="Laptop", price=999.99)
    print("Product:", product)

    settings = Settings()
    print("Settings:", settings)


if __name__ == "__main__":
    demo_serialization()