#1.LIST comprehension [...]
#old way in 3 lines code
classic_squares = []
for num in range(1, 6):
    classic_squares.append(num*num)
    
#list comprehenstion in one line
pythonic_squares = [num * num for num in range(1, 6)]
print(f"List Comprehension: {pythonic_squares}")


even_squares = [num * num for num in range(1 ,6) if num % 2 == 0]
print(f"Filtered List comprehension: {even_squares}")



#2.DICTIONARY comprehension
servers = ["web-01", "db-01", "cache-01"]

server_status ={server: "offline" for server in servers}
print(f"\nDict Comprehension: {server_status}")


#3.SET comprehension
messy_ips = ["192.168.1.1", "10.0.5", "192.168.1.1", "10.0.0.5", "172.16.0.1"]


unique_ips = (ip for ip in messy_ips)
print(f"\nSet comprehension (Duplicate removed!): {unique_ips}")