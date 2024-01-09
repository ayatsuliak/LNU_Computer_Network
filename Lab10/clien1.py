import socket#Імпортує модуль socket, який дозволяє використовувати сокети для мережевого взаємодії.

def start_client():#визначає функцію start_client, яка буде викликатися для запуску клієнта.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Створює сокет для використання з TCP/IP, вказуючи AF_INET для використання IPv4 та SOCK_STREAM для TCP.

    server_address = '127.0.0.1'  #Задає IP-адресу сервера. У цьому випадку це локальний адрес (localhost або 127.0.0.1).
    server_port = 5678  #Задає порт сервера, на якому слухає з'єднання.

    client.connect((server_address, server_port))#Встановлює з'єднання з сервером, використовуючи задану IP-адресу та порт.
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    #Відправляє логін та пароль на сервер, закодовані в байтах з використанням UTF-8.
    client.send(f"{login},{password}".encode('utf-8'))

    #Очікує відповідь від сервера (не більше 1024 байт) і декодує її з формату UTF-8.
    response = client.recv(1024).decode('utf-8')
    print(response)#Виводить отриману відповідь на екран.

    #Закриває з'єднання з сервером.
    client.close()

if __name__ == "__main__":
    start_client()#Викликає функцію start_client для запуску клієнта.
