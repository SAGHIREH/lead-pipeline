import httpx
import hmac
import hashlib
import uuid
import json
import time

url = "http://localhost:5678/webhook/v1/leads"
secret = "my_super_secret_key_123"

with open("tests/fixtures/valid-lead.json", "r", encoding="utf-8") as file:
    data = json.load(file)

body = json.dumps(data, separators=(',', ':'))
secret_bytes = secret.encode('utf-8')
body_bytes = body.encode('utf-8')
signature = hmac.new(secret_bytes, body_bytes, hashlib.sha256).hexdigest()

latencies = [] 

print("Starting load test (20 requests)...")

for i in range(20):
    idempotency_key = str(uuid.uuid4())
    headers = {
        "Content-Type": "application/json",
        "X-Signature": signature,
        "Idempotency-Key": idempotency_key
    }
    
    start_time = time.time()
    try:
        response = httpx.post(url, content=body, headers=headers, timeout=10.0)
        end_time = time.time()
        latency = (end_time - start_time) * 1000
        latencies.append(latency)
        print(f"Request {i+1}: Status Code {response.status_code} | Time: {latency:.2f} ms")
    except Exception as e:
        print(f"Request {i+1}: Error - {e}")

if latencies:
    latencies.sort()
    p95_index = int(len(latencies) * 0.95)
    p95_latency = latencies[p95_index]
    print("\n--- Final Results ---")
    print(f"Successful requests: {len(latencies)}")
    print(f"P95 Latency: {p95_latency:.2f} ms")