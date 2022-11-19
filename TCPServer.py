from socket import *

def server_code():
  # coding: UTF-8
  # サーバを作成
  serverPort = 50000
  serverAddress = '127.0.0.1'
  # AF = IPv4 という意味
  # TCP/IP の場合は、SOCK_STREAM を使う
  serverSocket = socket(AF_INET, SOCK_STREAM)

  # IPアドレスとポートを指定
  serverSocket.bind((serverAddress, serverPort))
  # 1 接続
  serverSocket.listen(1)
  print('The server is ready to receive')
  # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
  connectionSocket, addr = serverSocket.accept()
  # connection するまで待つ
  print("Connection from:" + str(addr))
  while True:
      # データを受け取る
      sentence = connectionSocket.recv(4096).decode()
      if not sentence:
        # if data is not received break
        break
      print("from Client : "+ str(sentence) )
      data = input(' -> ')
      # capitalizedSentence = sentence.upper()
      # クライアントにデータを返す
      connectionSocket.send(data.encode())
  connectionSocket.close()

if __name__ == '__main__':
  server_code()
