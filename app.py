from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# ---------------------------------------------------
#   Create FastAPI App
# ---------------------------------------------------
app = FastAPI(
    title="Calculator App",
    description="A simple FastAPI calculator supporting N number inputs",
    version="1.0.0"
)

# ---------------------------------------------------
#   Entry Route (Home)
# ---------------------------------------------------
@app.get("/")
def home():
    return {"message": "Calculator App"}


# ---------------------------------------------------
#   Input Model for N numbers
# ---------------------------------------------------
class Numbers(BaseModel):
    numbers: List[float]


# ---------------------------------------------------
#   ADD N NUMBERS
# ---------------------------------------------------
@app.post("/add-numbers")
def add_numbers(nums: Numbers):
    return {"operation": "addition", "result": sum(nums.numbers)}


# ---------------------------------------------------
#   MULTIPLY N NUMBERS
# ---------------------------------------------------
@app.post("/multiply-numbers")
def multiply_numbers(nums: Numbers):
    result = 1
    for num in nums.numbers:
        result *= num
    return {"operation": "multiplication", "result": result}


# ---------------------------------------------------
#   SUBTRACT N NUMBERS (first - rest)
# ---------------------------------------------------
@app.post("/subtract-numbers")
def subtract_numbers(nums: Numbers):
    values = nums.numbers
    if not values:
        return {"error": "No numbers provided"}

    result = values[0]
    for v in values[1:]:
        result -= v

    return {"operation": "subtraction", "result": result}


# ---------------------------------------------------
#   DIVIDE N NUMBERS (first / rest)
# ---------------------------------------------------
@app.post("/divide-numbers")
def divide_numbers(nums: Numbers):
    values = nums.numbers
    if not values:
        return {"error": "No numbers provided"}

    result = values[0]
    for v in values[1:]:
        if v == 0:
            return {"error": "Cannot divide by zero"}
        result /= v

    return {"operation": "division", "result": result}