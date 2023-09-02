# Python Peer-to-Peer Chat App with File Transfer

This is a Peer-to-Peer (P2P) Chat Application with file transfer functionality built using Python sockets. It allows a maximum of 5 clients to connect to the server simultaneously, exchange text messages, and efficiently send any type of file. This README will guide you through the setup, usage, and architecture of the application.  
<br>   

## Table of Contents

#### 1. [Requirements](#requirements)
#### 2. [Installation](#installation)
#### 3. [Usage](#usage)
#### 4. [Features](#features)
#### 5. [Architecture](#architecture)
#### 6. [Troubleshooting](#troubleshooting)
#### 6. [Screenshots](#screenshots)
#### 7. [Contributing](#contributing)
#### 8. [License](#license)  
<br>


## <a name="requirements">Requirements</a>

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Basic knowledge of Python and socket programming.
- A stable network connection for peer-to-peer communication.
<br>


## <a name="installation">Installation</a>

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python-Peer-to-Peer-chat-app-with-file-transfer-main
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

4. Install the required dependencies:

    ```bash
    pip install python-socketio
    pip install tqdm
    ```
<br>   



## <a name="usage">Usage</a>

1. Start the server:

    ```bash
    python server.py
    ```

   The server will start listening for incoming connections on a default port (i.e., 1080). You can customize the port by modifying `server.py` and in `clinet.py`.

   **Note: Server and clients must have the same port mentioned.**  


3. Start the client:

    ```bash
    python client.py
    ```

   You can run the client on multiple machines to connect to the server. Each client will need to provide the server's IP address and port.

4. Use the chat interface to send and receive text messages. Enter `!get_manual` to see the manual and available commands.

5. To send a file, use the `!send_file` command. For example:

    ```
    !send_file
    ```

   The server will handle the file transfer, and the save the file in the server.
<br>   



## <a name="features">Features</a>

- **Peer-to-Peer Chat**: Multiple clients can connect to the server and exchange text messages in real-time.

- **File Transfer**: Send any type of file to server efficiently and securely.

- **Basic Command Support**: Use commands like `!get_manual` to get the manual and list of available commands.

- **User-Friendly Interface**: Simple and intuitive command-line interface for ease of use.
<br>   


## <a name="architecture">Architecture</a>

The application is built using Python sockets and follows a client-server architecture.

- **Server**: The server acts as a central point for all clients. It manages client connections, relays messages between clients, and handles file transfers. It listens for incoming connections on a specified port and communicates with clients via sockets.

- **Client**: Clients connect to the server, send and receive messages, and can request file transfers. Each client runs on a separate machine and communicates with the server using sockets.

- **File Transfer**: File transfer is achieved by encoding the file into bytes, sending it in chunks, and decoding it on the receiving end. The server acts as an intermediary, ensuring the secure transfer of files between clients.
<br>   


## <a name="troubleshooting">Troubleshooting</a>

- **Port Conflicts**: If you encounter port conflicts, you can change the server's port in `server.py` and also be sure to change the client's port in `client.py` .

- **Firewall Issues**: Ensure that your firewall allows incoming and outgoing connections on the chosen port.

- **Client Connection Issues**: Make sure the server is running and reachable from the client machine. Verify that the IP address and port in `client.py` are correct.

- **File Transfer Failures**: If file transfers fail, check the file path and permissions on both the sender and receiver sides.
<br>   


## <a name="screenshots">Screenshots</a>
Start the server
![Start the server](https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer/blob/1dae80ee41a7097ce13f4d6804dd943f5ab6a215/screenshots/Screenshot%202023-08-21%20183318.png)

<br> 

Connect the client to the server's IP
![Connect the client to the server's IP](https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer/blob/1dae80ee41a7097ce13f4d6804dd943f5ab6a215/screenshots/Screenshot%202023-08-21%20183440.png)

<br> 

See the maual using `!get_manual` command
![See the maual](https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer/blob/1dae80ee41a7097ce13f4d6804dd943f5ab6a215/screenshots/Screenshot%202023-08-21%20183732.png)

<br> 

Send a file to the server using `!send_file` command
![Send a file to the server](https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer/blob/1dae80ee41a7097ce13f4d6804dd943f5ab6a215/screenshots/Screenshot%202023-08-21%20183913.png)

<br> 

The file is then saved in the same directory where the server file is located.
![The file is then saved in the same directory](https://github.com/SourabhBera/Python-Peer-to-Peer-chat-app-with-file-transfer/blob/1dae80ee41a7097ce13f4d6804dd943f5ab6a215/screenshots/Screenshot%202023-08-21%20183938.png)

<br>   


## <a name="contributing">Contributing</a>

Contributions are welcome! If you want to contribute to this project, please fork the repository and submit a pull request.  
<br>   



## <a name="license">License</a>
This project is licensed under the MIT License [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE). See the file for details [MIT License](LICENSE).


---  
<br>   

Feel free to reach out with any questions or feedback. Happy chatting and file sharing with the P2P Chat App!
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to reach out to us with any questions or feedback. Happy chatting and file sharing with the P2P Chat App!

