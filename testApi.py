import requests
import json

# Test cases from the document
test_cases = [
    {
        "name": "Example A",
        "data": ["a", "1", "334", "4", "R", "$"],
        "expected_odd": ["1"],
        "expected_even": ["334", "4"],
        "expected_alphabets": ["A", "R"],
        "expected_special": ["$"],
        "expected_sum": "339"
    },
    {
        "name": "Example B", 
        "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"],
        "expected_odd": ["5"],
        "expected_even": ["2", "4", "92"],
        "expected_alphabets": ["A", "Y", "B"],
        "expected_special": ["&", "-", "*"],
        "expected_sum": "103"
    },
    {
        "name": "Example C",
        "data": ["A", "ABcD", "DOE"],
        "expected_odd": [],
        "expected_even": [],
        "expected_alphabets": ["A", "ABCD", "DOE"],
        "expected_special": [],
        "expected_sum": "0"
    }
]

def test_api(base_url="http://localhost:8000"):
    """Test the API with the provided test cases"""
    
    for test_case in test_cases:
        print(f"\n--- Testing {test_case['name']} ---")
        
        payload = {"data": test_case["data"]}
        
        try:
            response = requests.post(f"{base_url}/bfhl", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Status: {response.status_code}")
                print(f"Request: {payload}")
                print(f"Response: {json.dumps(result, indent=2)}")
                
                print(f"Odd numbers: {result.get('odd_numbers')} (Expected: {test_case['expected_odd']})")
                print(f"Even numbers: {result.get('even_numbers')} (Expected: {test_case['expected_even']})")
                print(f"Sum: {result.get('sum')} (Expected: {test_case['expected_sum']})")
                
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    print("Testing API locally...")
    test_api("http://localhost:8000")