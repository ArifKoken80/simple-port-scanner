# 🔍 Simple Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Threads](https://img.shields.io/badge/Threads-200-00ff9c?style=flat-square)
![Purpose](https://img.shields.io/badge/Purpose-Educational-orange?style=flat-square)

A fast, multi-threaded TCP port scanner written in pure Python. It finds open ports on a target, identifies common services, grabs service banners and exports the results to TXT and CSV.

---

## ✨ Features

- ⚡ **Multi-threaded scanning:** 200 concurrent workers via `ThreadPoolExecutor`
- 🔎 **Service detection:** maps common ports (FTP, SSH, Telnet, SMTP, DNS, HTTP/S, POP3, IMAP, MySQL, HTTP-ALT)
- 🏷️ **Banner grabbing:** reads service banners to fingerprint what is running
- 💾 **Result export:** saves findings to `scan_results.txt` and `scan_results.csv`
- ⏱️ **Scan timing:** reports total scan duration
- 📦 **No dependencies:** uses only the Python standard library

---

## 🚀 Usage

```bash
python main.py
```

```text
Target IP: 192.168.1.10
Start Port: 1
End Port: 1000

Scanning 192.168.1.10...

[+] 22/tcp OPEN | SSH | SSH-2.0-OpenSSH_8.9p1
[+] 80/tcp OPEN | HTTP | No banner

[+] Results saved to scan_results.txt and scan_results.csv

Scan finished in 6.42 seconds
```

*(Example output; results depend on the target.)*

---

## 🧠 How It Works

1. Takes the target IP and port range from the user
2. Sends each port to a thread pool and tries a TCP connection (`connect_ex`)
3. For open ports, looks up the service name and attempts banner grabbing
4. Collects the results and writes them to TXT and CSV files

---

## 🗺️ Roadmap

- [x] Port range scanning
- [x] Multi-threading
- [x] Service detection & banner grabbing
- [x] TXT / CSV export
- [ ] Command-line arguments (`--host`, `--ports`, `--threads`)
- [ ] JSON export
- [ ] UDP scanning

---

## ⚠️ Disclaimer

This tool is for **educational purposes and authorized testing only**. Only scan systems you own or have explicit permission to test.

---

👨‍💻 **Author:** [Arif Köken](https://github.com/ArifKoken80)
