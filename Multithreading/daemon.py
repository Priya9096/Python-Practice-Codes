import threading
import time

def background_task():
    print(threading.current_thread())
    while True:
        time.sleep(1)
        print("Background task running...")

thread = threading.Thread(target=background_task, name = 'daemon')
thread.daemon = True 
thread.start()

time.sleep(3)
print("Main Thread is Dead.")