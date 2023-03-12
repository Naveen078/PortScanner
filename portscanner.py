import socket
from threading import Thread, Lock

# Get the target host from user input
target_host = input("Enter the host to scan: ")

# Get the port range from user input
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

# Create a lock object to synchronize threads
lock = Lock()

# Define a function to scan a range of ports
def scan_port(port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout to avoid blocking
        sock.settimeout(0.5)
        # Connect to the target host and port
        result = sock.connect_ex((target_host, port))
        # If the connection is successful, print the open port
        if result == 0:
            with lock:
                print(f"Port {port} is open")
        # Close the socket
        sock.close()
    except:
        pass

# Create a list of threads to scan each port
threads = []
for port in range(start_port, end_port+1):
    thread = Thread(target=scan_port, args=(port,))
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to finish
for thread in threads:
    thread.join()
