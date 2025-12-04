from typing import Optional
from pydantic import BaseModel, EmailStr, constr, model_validator


# -------- User Schemas --------

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=1, max_length=128)


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


# -------- Calculation Schemas --------

class CalculationBase(BaseModel):
    a: float
    b: float
    type: str  # "Add", "Sub", "Multiply", "Divide"
    user_id: Optional[int] = None


class CalculationCreate(CalculationBase):
    # Pydantic v2-style validator that runs after the model is built
    @model_validator(mode="after")
    def check_divide_by_zero(self):
        # make type check case-insensitive so "divide" and "Divide" both work
        if self.type and self.type.lower() == "divide" and self.b == 0:
            # This ValueError is wrapped into a ValidationError by Pydantic
            raise ValueError("Cannot divide by zero")
        return self


class CalculationRead(CalculationBase):
    id: int
    result: Optional[float] = None

    class Config:
        from_attributes = True
# --- Auth-related user schemas ---
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserLogin(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        # Pydantic v1 style for SQLAlchemy models
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
