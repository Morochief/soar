import os
import sys
import json

def analyze_alert():
    alert_raw = {
        "device": "FG-Technoma",
        "policyname": "Block_WIFI-Corp",
        "policyid": 214,
        "dstport": 853,
        "service": "Fortinet-FortiGuard",
        "dstip": "96.45.46.46",
        "date": "2026-09-27",
        "state": "Closed",
        "anomaly": "External Firewall Denial Anomaly"
    }
    print("Alert Analysis:")
    print(f"Policy: {alert_raw['policyname']} (ID {alert_raw['policyid']})")
    print(f"Port: {alert_raw['dstport']} (DNS-over-TLS / DoT)")
    print(f"State in JSON: {alert_raw['state']}")
    print(f"Date: {alert_raw['date']}")

if __name__ == "__main__":
    analyze_alert()
