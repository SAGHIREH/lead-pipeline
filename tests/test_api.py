import httpx
import hmac
import hashlib
import uuid
import json

url = "http://localhost:5678/webhook/v1/leads"
secret = "my_super_secret_key_123"

with open("tests/fixtures/valid-lead.json", "r", encoding="utf-8") as file:
    data = json.load(file)

body = json.dumps(data, separators=(',', ':'))

secret_bytes = secret.encode('utf-8')
body_bytes = body.encode('utf-8')
signature = hmac.new(secret_bytes, body_bytes, hashlib.sha256).hexdigest()

idempotency_key = str(uuid.uuid4())
headers = {
    "Content-Type": "application/json",
    "X-Signature": signature,
    "Idempotency-Key": idempotency_key
}

print("Sending request...")
try:
    response = httpx.post(url, content=body, headers=headers)
    
    if response.status_code == 200:
        print("✅ SUCCESS! Status Code: 200")
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("⚠️ Server returned an empty response.")
            print(f"Raw response: '{response.text}'")
    else:
        print(f"❌ ERROR! Status Code: {response.status_code}")
        print(response.text)

except httpx.RequestError as exc:
    print(f"Error connecting to the server: {exc}")