import threading
import time
import random

def thread_print(thread_id):
    
    print(f"Hi, I’m thread {thread_id}")

    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)

    print(f"Thread {thread_id} ended after sleeping for {sleep_time} seconds")

def main():
    threads = []

    for i in range(3):
        thread = threading.Thread(target=thread_print, args=(i,))
        threads.append(thread)
        thread.start()

if __name__ == "__main__":
    main()
