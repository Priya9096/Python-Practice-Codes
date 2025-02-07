import threading
import time

def count_task(task_name, count_limit):
    print(f"Starting count for {task_name} up to {count_limit}...")
    for i in range(1, count_limit + 1):
        print(f"{task_name}: {i}")
        time.sleep(0.5) 
    print(f"Counting task for {task_name} completed.")

user_input = input().strip()
tasks = user_input.split(", ")

threads = []
for task in tasks:
    name, count = task.split("-")
    count_limit = int(count)
    thread = threading.Thread(target=count_task, args=(name, count_limit))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
