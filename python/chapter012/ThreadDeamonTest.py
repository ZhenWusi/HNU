import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)       
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')

if __name__ == '__main__':
    print("main thread")
    t = threading.Thread(target=run, args=("t1",))
    #t.setDaemon(True)
    t.daemon = True   
    t.start()
    print("main thread end")