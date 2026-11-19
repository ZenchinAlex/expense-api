from fastapi import FastAPI
from pydantic  import BaseModel

app = FastAPI()

class Expense(BaseModel):
    category: str
    amount: float


expenses_db = []


@app.post("/expenses")
def create_expense(expense: Expense):
    expenses_db.append(expense)
    return expense


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/expenses")
def expenses():
    return expenses_db


    