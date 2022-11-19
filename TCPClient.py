# coding: UTF-8
# クライアントを作成

from socket import *

def client():
    serverAddress = '127.0.0.1'
    serverPort = 50000

    # AF = IPv4 という意味
    # TCP/IP の場合は、SOCK_STREAM を使う
    #ソケットの作成(socket)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # サーバを指定(connect)
    clientSocket.connect((serverAddress, serverPort))
    sentence = input(' -> ')

    while sentence.lower().strip() != 'bye':

      # サーバにメッセージを送る(send)
      clientSocket.send(sentence.encode())
      # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
      data = clientSocket.recv(4096).decode()
      print('From Server: ', data)
      sentence = input(" -> ")

    #ソケットをクローズ(close)
    clientSocket.close()


if __name__ == '__main__':
  client()
