import socket

domain = 'www.google.com'

# Resolve IP address
ip = socket.gethostbyname(domain)
print("IP Address:", ip)

# For more advanced lookups, you can use 'dnspython'
import dns.resolver

answers = dns.resolver.resolve(domain, 'A')
for rdata in answers:
    print("A record:", rdata.to_text())
