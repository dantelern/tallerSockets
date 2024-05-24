import socket

def server():
    # Obtener el hostname
    host = socket.gethostname()

    # Especificar el puerto para escuchar
    # TO DO
    port = 4000

    # Crear un objeto socket
    s = socket.socket()

    # Bindear el socket al host y al puerto
    s.bind((host, port))

    # Escuchar conexiones ingresantes
    # TO DO
    s.listen(1)
    # Aceptar conexiones entrantes
    c, address = s.accept()
    print(f"Connected to: {address}")

    newMsg = True
    while newMsg:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = c.recv(1024).decode()

        if not data:
            # Si no hay data, romper el ciclo
            newMsg = False
            print("No data received. Closing connection.")
            break

        # setear en newMsg si hay data nueva (si no, rompe el ciclo)
       
        print(f"Recibido de cliente: {data}")

        # Obtener el input de usuario y enviar al cliente (usar response.encode())
        response = input("Enter response to send to client: ")
        # TO DO
        c.send(response.encode())

    # Cerrar la conexión con el cliente
    c.close()
    s.close()

if __name__ == "__main__":
    # Start the server
    server()


