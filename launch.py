import os, time, threading
def delete():
  time.sleep(10)
thread = threading.Thread(target=delete)
thread.start()
os.system("firefox")