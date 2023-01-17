import socket
from threading import Thread

interface = dict(
    host="192.168.1.6",
    port=3333
)

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)


def main_loop():
    with sock as s:
        s.bind(tuple(interface.values()))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                conn.sendall(b"Hello")


if __name__ == '__main__':
    keyboard_interrupt = Thread()
    loop = Thread(target=main_loop)
    loop.start()
