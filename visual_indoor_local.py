import socket
import json
import matplotlib.pyplot as plt

host_ip = "192.168.0.113"
port = 8787

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((host_ip, port))

x_coord = []
y_coord = []

plt.ion()
fig = plt.figure(figsize=(3,3))
#ax = fig.subplots(1,1)
while True:
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    try:
        data_json = json.loads(data)
    except:
        print("fail to load data")
        continue
    
    x_coord.append(data_json["x_coord"])
    y_coord.append(data_json["y_coord"])
    x_coord = x_coord[-20:]
    y_coord = y_coord[-20:]
    fig.clear()
    plt.plot(x_coord, y_coord)
    plt.show()
    plt.pause(0.0001)
