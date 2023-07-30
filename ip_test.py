import socket

hostname = socket.gethostname()
ip_addresses = socket.getaddrinfo(hostname, None)
ipv4_addresses = [addr[4][0] for addr in ip_addresses if ':' not in addr[4][0]]

print(ipv4_addresses)