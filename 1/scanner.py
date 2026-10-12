import socket
import sys
from datetime import datetime
import threading
from queue import Queue

# 로컬주소입니다. 바꾸면 불법댐
target_host = "127.0.0.1"
print_lock = threading.Lock()
queue = Queue()

print("=" * 50)
print(f"포트조사 가동")
print(f"대상 IP : {target_host}")
print(f"시작 시간: {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
print("=" * 50)
print(f" {target_host}의 모든 포트를 검사 중입니다. 잠시만 기다려주세요...\n")


def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1) # 로컬은 0.1, 국내 외부 서버는 1.0, 해외는 2.0
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            with print_lock:
                print(f"[OPEN] 포트 {port:5}번이 열려 있습니다!")
        s.close()
    except:
        pass

def thread_worker():
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

for port in range(1, 65536):
    queue.put(port)

thread_list = []
for _ in range(500):
    thread = threading.Thread(target=thread_worker)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

print("\n" + "=" * 50)
print("조사완료.")
print("=" * 50)
