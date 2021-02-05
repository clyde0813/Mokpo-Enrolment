import multiprocessing
import socket
import logging
import os

HOST = "0.0.0.0"
PORT = 9999

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('data.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def handle(connection, address):
    try:
        while True:
            pn = connection.getpeername()
            logger.info(str(pn))
            data = connection.recv(1024)
            logger.info(data.decode("utf-8"))
    except ConnectionResetError:
        connection.close()


class Server(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            process = multiprocessing.Process(
                target=handle, args=(conn, address))
            process.daemon = True
            process.start()


if __name__ == "__main__":
    server = Server(HOST, PORT)
    try:
        logger.info('서버 구동중')
        server.start()
    except Exception as ec:
        print(ec)
    finally:
        for process in multiprocessing.active_children():
            process.terminate()
            process.join()
