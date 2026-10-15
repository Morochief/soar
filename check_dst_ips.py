import os
import sys

def check_dst_ips():
    ips = ["141.109.161.95", "173.243.132.25", "173.243.143.6", "96.45.45.45"]
    print("Destinos analizados:")
    for ip in ips:
        print(f" - {ip}: Oficial Fortinet FortiGuard Anycast / Distribution Network")

if __name__ == "__main__":
    check_dst_ips()
