import socket

def client():
    # Obtener el hostname (ya que tanto cliente como servidor correrán en tu máquina)
    host = socket.gethostname()

    # Definir el número de puerto para comunicarse con el servidor
    port = 4000

    # Crear un objeto socket
    client_socket = socket.socket()

    # Conectar al servidor especificando el hostname y el puerto
    client_socket.connect((host, port))

    # Pedir al usuario un input
    message = input("Ingresá un mensaje (Poner 'chau' para salir): ")

    while message.lower().strip() != "chau":
        # Enviar el mensaje al server (usar message.encode())
        client_socket.send(message.encode())
       
        # Recibir una respuesta del servidor
        data = client_socket.recv(1024).decode()

        # Mostrar el mensaje recibido del servidor
        print("Received from server: " + data)
       
        # Pedir un nuevo mensaje
        message = input("Ingresá un mensaje (Poner 'chau' para salir): ")

    # Cerrar la conexión
    client_socket.close()

if __name__ == "__main__":
    client()