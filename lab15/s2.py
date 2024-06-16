import select
import socket
import requests
import json

HOST = '127.0.0.1'
PORT = 6667
API_KEY = 'd4af3e33095b8c43f1a6815954face64'
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q=Lublin&appid={API_KEY}&units=metric'


def get_weather():
    response = requests.get(WEATHER_URL)
    if response.status_code == 200:
        data = response.json()
        weather_info = f"Lublin: {data['main']['temp']}°C, {data['weather'][0]['description']}"
        return weather_info
    return "Nie można pobrać danych pogodowych"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
server_socket.setblocking(0)

inputs = [server_socket]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server_socket:
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(0)
            inputs.append(client_socket)
            message_queues[client_socket] = []
        else:
            data = s.recv(1024)
            if data:
                weather_info = get_weather().encode()
                message_queues[s].append(weather_info)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].pop(0)
        except IndexError:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
