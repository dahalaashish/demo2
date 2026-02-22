# scanner.py

import socket

# Common port-service mapping
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown Service")
            return (port, service)
        else:
            return None

    except socket.error:
        return None


def scan_range(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        result = scan_port(target, port)
        if result:
            open_ports.append(result)

    return open_ports