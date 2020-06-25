import datetime
import json
import socket

HOST = "localhost"
PORT = 8889
BUFFER_SIZE = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()

    with connection:

        while True:

            # Assume we got HTTP request
            data: str = connection.recv(BUFFER_SIZE).decode("utf-8").strip()

            if "GET /close HTTP/1.1" in data:
                print("Closing connection")
                break

            if "HTTP/1.1" in data:
                http_request_headers: dict = {}
                headers = data.split(sep="\r\n")
                for i, header in enumerate(headers):
                    # Skip request type
                    if i == 0:
                        continue
                    header_name = header.split(sep=":")[0].strip()
                    header_value = header.split(sep=":")[1].strip()
                    http_request_headers[header_name] = header_value
                content = json.dumps(http_request_headers)
                current_datetime = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
                server_response: str = f"""HTTP/1.1 200 OK
Server: Otus
Date: {current_datetime}
Content-Length: {len(content)}
Content-Type: application/json
Connection: Closed

{content}
"""
                connection.send(server_response.encode("utf-8"))
#
