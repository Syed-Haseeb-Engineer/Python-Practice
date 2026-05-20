from functools import reduce

servers = ["web-1", "db-01", "cache-01"]
ips = ["192.168.1.5", "10.0.0.12", "172.16.0.4"]

print("--- Enumerate ----")
for index, server in enumerate(servers):
    print(f"Item {index}: {server}")

print("\n--- Zip ---")
for server, ip in zip(servers,ips):
    print(f"server {server} is at {ip}")

upper_servers = list(map(lambda s: s.upper(), servers))
print(f"\nMap Result: {upper_servers}")

local_ips = list(filter(lambda ip: ip.startswith("192"), ips))
print(f"\nFilter Result: {local_ips}")

numbers = [1,2,3,4]
product = reduce(lambda x,y: x * y, numbers)
print(f"\nReduce Result: {product}")