from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI(title="BFHL API", description="Bajaj Finserv Health Answer API", version="1.0.0")

# Request
class DataRequest(BaseModel):
    data: List[str]

# Response
class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str

def process_data(data: List[str]) -> dict:
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    numbers_for_sum = []
    
    for item in data:
        if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
            num = int(item)
            numbers_for_sum.append(num)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        
        elif item.isalpha():
            alphabets.append(item.upper())
        
        elif re.match(r'^[a-zA-Z]+$', item):
            alphabets.append(item.upper())
        
        else:
            if re.match(r'^[a-zA-Z]+$', item):
                alphabets.append(item.upper())
            else:
                special_characters.append(item)
    
    total_sum = sum(numbers_for_sum)
    
    all_alphabets = []
    for alphabet in alphabets:
        for char in alphabet:
            all_alphabets.append(char)
    
    all_alphabets.reverse()
    
    concat_string = ""
    for i, char in enumerate(all_alphabets):
        if i % 2 == 0:
            concat_string += char.lower()
        else:
            concat_string += char.upper()
    
    return {
        "is_success": True,
        "user_id": "hrishikesh_arun_13052005",
        "email": "hrishikeshvirupakshi@gmail.com",  
        "roll_number": "22BCE1817",  
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }

@app.post("/bfhl", response_model=DataResponse)
async def process_bfhl_data(request: DataRequest):
    try:
        if not request.data:
            raise HTTPException(status_code=400, detail="Data array cannot be empty")
        
        result = process_data(request.data)
        return DataResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/bfhl")
async def get_operation_code():
    return {
        "operation_code": 1
    }

@app.get("/")
async def root():
    return {
        "message": "BFHL API is running",
        "endpoints": {
            "POST /bfhl": "Process data array",
            "GET /bfhl": "Get operation code"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)