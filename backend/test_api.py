import urllib.request
import json
import time

# Sleep removed
# time.sleep(2)

url = "http://127.0.0.1:8000/analyze"
data = {
    "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
    "analysis_type": "Review"
}

try:
    req = urllib.request.Request(
        url, 
        data=json.dumps(data).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}, 
        method='POST'
    )
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(result)

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
