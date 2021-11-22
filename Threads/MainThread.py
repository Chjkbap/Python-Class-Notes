import threading

trd = threading.current_thread().getName()# invoke the current_thread method for info about current thread
print(f"This is the current thread {trd}")

# if threading.current_thread() == threading.main_thread():
#     print("This is the main thread")
# else:
#     print("Not the main thread")