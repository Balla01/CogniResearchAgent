import sys
import socket

def check_internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print(f"Successfully connected to {host}:{port}")
        return True
    except socket.error as ex:
        print(f"Could not connect to {host}:{port}. Error: {ex}")
        return False

if __name__ == "__main__":
    if check_internet():
        print("Internet access is available.")
        sys.exit(0)
    else:
        print("Internet access is NOT available.")
        sys.exit(1)
