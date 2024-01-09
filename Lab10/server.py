import socket #Імпортує модуль socket, який дозволяє використовувати сокети для мережевого взаємодії.
import threading # Імпортує модуль threading для використання потоків, які дозволяють обробляти з'єднання в паралельному режимі.


def handle_client(client_socket):#Визначає функцію handle_client, яка обробляє дані від клієнта.
    thread_id = threading.current_thread().ident
    print(f"[INFO] Обробка клієнта у потоці {thread_id}")
    data = client_socket.recv(1024).decode('utf-8')#Отримує дані від клієнта (не більше 1024 байт) і декодує їх з формату UTF-8.
    login, password = data.split(',')#Розділяє отримані дані на дві частини за допомогою коми, припускаючи, що дані представлені у форматі "логін,пароль".

    #Логіка аутентифікації та відправлення вітання: Перевіряє, чи логін та пароль співпадають з певними значеннями. Якщо так, відправляє вітання, інакше відправляє повідомлення про помилку.
    if login == 'Andrii' and password == '1234':
        client_socket.send("Вітаю, Andrii Yatsuliak!".encode('utf-8'))
    else:
        client_socket.send("Помилковий логін чи пароль.".encode('utf-8'))

    # Закрити з'єднання з клієнтом
    client_socket.close()


def start_server(mode='sequential'):#Визначає функцію start_server, яка налаштовує та слухає сокет.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Створює сокет для використання з TCP/IP, вказуючи AF_INET для використання IPv4 та SOCK_STREAM для TCP.
    server.bind(('0.0.0.0', 5678))  #Прив'язує сокет до IP-адреси та порту. У цьому випадку слухається адреса '0.0.0.0' (всі доступні мережі) на порту 12345.
    server.listen(5)#Розпочинає слухання на вказаному порті, обмежуючи кількість з'єднань черги до 5.

    print("[INFO] Сервер слухає порт 5678...")

    while True:#Безкінечний цикл, що чекає на з'єднання від клієнтів.
        client, addr = server.accept()#Приймає вхідне з'єднання, і client - це новий сокет для взаємодії з клієнтом, addr - адреса клієнта.
        print("[INFO] З'єднання від", addr)#Визначає, як обробляти з'єднання - послідовно або паралельно.

        if mode == 'sequential':
            handle_client(client)# Викликає функцію обробки клієнта у послідовному режимі.
        elif mode == 'parallel':#Якщо вказано режим паралельної обробки.
            client_handler = threading.Thread(target=handle_client, args=(client,))#Створює новий потік для обробки клієнта.
            client_handler.start()# Запускає потік для обробки клієнта.


if __name__ == "__main__":
    server_mode = input("Введіть режим сервера (sequential/parallel): ").lower()#Запитує користувача ввести режим сервера (послідовний або паралельний).
    start_server(server_mode)#Запускає сервер у вказаному режимі.
