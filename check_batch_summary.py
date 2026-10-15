import json

# Let's inspect the alerts present in the dump:
# We saw:
# 1) Alert e3e4b331:
#    - srcip: 192.168.169.19 -> dstip: 10.11.1.1 (ad.technoma.local:53)
#    - query: release-assets.githubusercontent.com
#    - signature: "INFO Github CDN for Release Assets Domain in DNS Lookup (release-assets .githubusercontent .com)"
#    - display_name: "Private to Private Exploit Anomaly"
# 2) Alert 19cc2f05:
#    - srcip: 10.11.1.1 (ad.technoma.local) -> dstip: 8.8.8.8:53 (Google DNS)
#    - query: relay-7c3b6b0a.net.anydesk.com
#    - signature: "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup"
#    - display_name: "Private to Public Exploit Anomaly"
# 3) Alert e8ab17e9 & 8776124f & 94595bd6:
#    - srcip: 192.168.169.71 (NB-ICENTURION) -> dstip: 10.11.1.1:445 (ad.technoma.local:445 SMB)
#    - username: ivancenturion
#    - share: \\technoma.local\IPC$
#    - signatures: "INFO NTLM Session Setup Request - Auth", "INFO NTLM Session Setup Request - Negotiate", "INFO NTLMv1 Session Setup Response - Challenge"
#    - display_name: "Private to Private Exploit Anomaly"
# 4) Alert 2e271214 & af0b6344 & 99866173:
#    - srcip: 192.168.169.78 -> dstip: 10.11.1.1:53 & 8.8.4.4:53
#    - query: web.telegram.org, pluto.web.telegram.org, _5222._https.web.whatsapp.com
#    - signature: "INFO Observed Telegram Domain in DNS Lookup (telegram .org)"
#    - display_name: "Private to Private Exploit Anomaly" / "Private to Public Exploit Anomaly"
# 5) Alert e796ab7b & 95fe7ed8:
#    - ATH / Correlated playbook: "Exploited C&C Connection" (severity 75 / 82)
#    - Correlates the "exploit" (which is actually just an informational IDS signature INFO Telegram or INFO NTLM) with normal LDAP traffic on port 389 from 10.11.1.1 to 192.168.169.78 or 192.168.169.71!

def print_summary():
    print("Batch contains 5 groups of benign informational alerts misclassified as exploits by Stellar Cyber ML anomaly engine.")

if __name__ == "__main__":
    print_summary()
