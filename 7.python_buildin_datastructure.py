# # LISTS
# ubuntu_version =["20.04", "22.04"]
# print(f"Original List:{ubuntu_version}")

# ubuntu_version.append("24.04")
# print(f"Updated List: {ubuntu_version}")

# print(f"Current LTS: {ubuntu_version[2]}")

# #TUPLE
# db_config = ("localhost", 5432, "admin")
# print(f"\nDatabase Port: {db_config[1]}")

# try:
#     db_config[1]= 8080
# except TypeError as e:
#     print(f"As expected, Tuple blocked the change: {e}")



# #SET
# web_servers = {"192.168.1.10", "192.168.11", "192.168.1.12"}
# db_servers = {"192.168.1.12", "192.168.1.13"}

# messy_logs = ["error", "warning", "error", "info", "error"]
# unique_logs = set(messy_logs)
# print(f"Unique log type: {unique_logs}")

# hybridserver =web_servers.intersection(db_servers)
# print(f"Server acting as Web AND DB: {hybridserver}")

# all_infrastructure = web_servers.union(db_servers)
# print(f"All infrastruture IPs: {all_infrastructure}")


# #DICTIONARY
# linux_user = {
#     "username": "Haseeb",
#     "shell": "/bin/bash",
#     "sudo_priviledges": True,
#     "ssh_key": ["rsa_key1", "ed25519_key"]
# }

# print(f"User's shell: {linux_user['shell']}")

# linux_user["home_dir"] = "/home/Haseeb"
# print(f"Added home directory: {linux_user['home_dir']}")


# print(f"Missing key check: {linux_user.get('password', 'No Password Set!')}")

# print("\n--- User Profile Dump ---")
# for key, value in linux_user.items():
#     print(f"(key): {value}")



#String
filepath = "/var/log/syslong"

new_filepahth = "C" + filepath[1:]

print(new_filepahth)

print((f"Original: {filepath}"))

print(f"First 4 chars: {filepath[0:4]}")

print(f"Filename only: {filepath[-7:]}")

print(f"Reversed string: {filepath[::-1]}")

csv_line = "root,x,0,0,root,/root,/bin/bash"
parsed_data = csv_line.split(",") #Turn string into list
print(f"\nParsed CSV to List: {parsed_data}")