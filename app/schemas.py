from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class ExpenseUpdate(BaseModel):
    title: str
    amount: float
    category: str