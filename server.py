import socket
import threading
import time
import os
import tqdm


PORT = 1080 
HEADER = 2048
FORMAT = 'utf-8'

def start_chat(SERVER, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER,PORT))
    print(f'[CONNECTED] Connected to {SERVER}:{PORT} \n')
    print(f'Happy chatting with your family and friends. \nTo see the manual type: !get_manual  ')

    print('\n----------------------------------------------------------------------------\n')

    receive_thread = threading.Thread(target=receive_messages, daemon=True, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client, USER_NAME, ))
    send_thread.start()


class Manual:
    
    def manual(self):
        print(f'''
    Hello this is the manual page.

    The server runs on { SERVER } at Port { PORT }

    Enter:

        !disconnect -- To exit the chat and dissconnect with the server.

        !send_file -- To send a file to all the connected users.

        !active_users -- To see how many users are currently in the chat 
                         and connected to the server.

        !my_info -- To get your information.

----------------------------------------------------------------------------\n
    ''')


    def my_info(self):
        my_ip = socket.gethostbyname(socket.gethostname())
        print(f'''
    Username: { USER_NAME }
    Your IP: { my_ip }
    Server IP: { SERVER }
    Port: { PORT }
    Connection Status: Connected

    ''')
        

    def send_file(self, client):
        self.client = client
        file_path = input("Enter The file path: ")
        file_split = file_path.split('\\')
        file_name = file_split[-1:]
        try:
            file_size = os.path.getsize(file_path)
            progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(file_path, 'rb') as file:
                
                client.send(file_name[0].encode())
                client.send(str(file_size).encode())

                while True:
                    chunk = file.read(2048)  
                    if not chunk:
                        break  
                    client.send(chunk)
                    progress.update(len(chunk))
            print("\nFile sent successfully \n")
            return
        
        except Exception as e:
            print('\nSorry! This function is in development.\n')
        return


    def active_users(self, client):
        self.client = client
        client.send("!active_users".encode(FORMAT))



def rec_file(client):
    name_size = client.recv(1024).decode()
    name_size_split = name_size.split('#')
    file_name = str(name_size_split[0])
    file_size = int(name_size_split[1])
    data = b''
    while True:
        chunk = client.recv(file_size)
        if chunk == b'END':
            break  
        data += chunk 
        break
    name_size_split = name_size.split('#')
    file_name = str(name_size_split[0])
    file_size = int(name_size_split[1])
    
    print("\n\tFile name: ",file_name)
    print("\tFile size: ",file_size)

    with open(file_name, 'wb') as file: 
        file.write(data)

    print("\n\tFile received and saved.\n")



def receive_messages(client):
    while True:
        data = client.recv(2048).decode()
        new_data = data.split("#")

        if new_data[0] == '!active_users':
            print(f'\nActive Users: { new_data[1] } \n')
        
        elif new_data[0] == 'notify':
            print(new_data[1])
        
        elif new_data[0] == "message":
            if new_data[3] == 'quit':
                exit()
            else:
                print(f"\n{ new_data[1] } > {new_data[3]}")
        
            

def send_messages(client, USER_NAME):
    client.send(USER_NAME.encode())
    manual = Manual()
    msg = True
    while msg:
        message = input("Me > ")
        if message == '!get_manual':
            manual.manual()
            continue

        elif message == "!disconnect":
            client.send("quit".encode())
            msg=False

        elif message[:10] == "!send_file":
            client.send(message[:11].encode())
            manual.send_file(client)
            time.sleep(1)
            client.send("END".encode())
            continue

        elif message == "!active_users":
            manual.active_users(client)
            
        elif message == "!my_info":
            manual.my_info()
            continue
            
        elif message == "!rec_file":
            client.send("!rec_file".encode())
            rec_file(client)
            continue

        client.send(message.encode())
    



if __name__ == '__main__':
    SERVER = input("Enter the server IP: ")
    USER_NAME = input("Enter username: ")
    print(f'[INFO] Trying to connect the server at  {SERVER}:{PORT} ')
    start_chat(SERVER, PORT)

    
