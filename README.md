# Bajaj Finserv Health Limited | Full Stack | Qualifier 1

A REST API built with FastAPI that processes mixed data arrays and categorizes elements according to the assessment requirements.

## 📋 Problem Statement

Build a REST API (POST method) that takes an array of mixed data and returns:
- Separated odd/even numbers
- Alphabetic characters (uppercase)
- Special characters  
- Sum of numbers
- Concatenated alphabets in reverse order with alternating caps
- User information and success status

## 🚀 Solution Approach

**Tech Stack:** FastAPI + Python + Vercel

## 🛠 Setup & Run

```bash
# Create virtual environment (Python 3.11/3.12)
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

API runs at: `http://localhost:8000`

## 🧪 Testing

### Method 1: Using cURL

```bash
# Test Example A
curl -X POST "http://localhost:8000/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["a","1","334","4","R","$"]}'

# Expected Response
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### Method 2: Interactive Docs

1. Start server: `uvicorn main:app --reload`
2. Open: `http://localhost:8000/docs`
3. Test the POST `/bfhl` endpoint directly

## 🌐 Deployment

**Deployed on Vercel:** `https://bfhl-full-stack-qualifier.vercel.app/bfhl`

```bash
# Test deployed API
curl -X POST "https://bfhl-full-stack-qualifier.vercel.app/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["2","a","y","4","&","-","*","5","92","b"]}'
```

## 📁 Files

- `main.py` - FastAPI application with core logic
- `requirements.txt` - Python dependencies  
- `vercel.json` - Deployment configuration
- `test_api.py` - Automated test script

## ⚙️ Key Implementation Details

- **Numbers returned as strings** (as per requirements)
- **Error handling** for invalid inputs
- **Pydantic models** for request/response validation
- **Mixed string handling** (e.g., "ABcD" treated as alphabets)
- **Concatenation logic** with alternating caps in reverse order

---

**Note:** Update `user_id`, `email`, and `roll_number` in `main.py` before deployment.