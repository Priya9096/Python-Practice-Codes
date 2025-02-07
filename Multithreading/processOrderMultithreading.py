import threading
import time

def process_request(user):
    print(f"Processing request for {user}...")
    time.sleep(5)
    print(f"Request completed for {user}")

t1 = threading.Thread(target=process_request, args=("User 1",))
t2 = threading.Thread(target=process_request, args=("User 2",))
t3 = threading.Thread(target=process_request, args=("User 3",))

t1.start()
t2.start()
t3.start()