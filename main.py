import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import time

# -----------------------------
# SERVİS MAP (PORT → SERVICE)
# -----------------------------
SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

results = []

# -----------------------------
# BANNER GRABBING
# -----------------------------
def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))

        # küçük request gönder (bazı servisler cevap verir)
        sock.send(b"Hello\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()

        return banner if banner else "No banner"

    except:
        return "No banner"


# -----------------------------
# PORT SCAN
# -----------------------------
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = SERVICE_MAP.get(port, "Unknown")
            banner = grab_banner(ip, port)

            data = {
                "port": port,
                "status": "OPEN",
                "service": service,
                "banner": banner
            }

            print(f"[+] {port}/tcp OPEN | {service} | {banner}")

            results.append(data)

        sock.close()

    except:
        pass


# -----------------------------
# THREAD POOL SCANNER
# -----------------------------
def scan_range(ip, start_port, end_port, threads=100):
    print(f"\nScanning {ip}...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(scan_port, ip, port)
            for port in range(start_port, end_port + 1)
        ]

        for _ in as_completed(futures):
            pass


# -----------------------------
# SAVE RESULTS
# -----------------------------
def save_results():
    # TXT
    with open("scan_results.txt", "w") as f:
        for r in results:
            f.write(f"{r}\n")

    # CSV
    with open("scan_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["port", "status", "service", "banner"])
        writer.writeheader()
        writer.writerows(results)

    print("\n[+] Results saved to scan_results.txt and scan_results.csv")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    ip = input("Target IP: ")
    start = int(input("Start Port: "))
    end = int(input("End Port: "))

    start_time = time.time()

    scan_range(ip, start, end, threads=200)

    save_results()

    print(f"\nScan finished in {round(time.time() - start_time, 2)} seconds")