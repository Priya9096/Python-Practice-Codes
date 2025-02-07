import time
def process_request(user):
    print(f"Processing request for {user}...")
    time.sleep(5)
    print(f"Request completed for {user}")

process_request("User 1")
process_request("User 2")
process_request("User 3")