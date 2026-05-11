import copy

print("--- 1. The Assignment Trap ----")
original = ["Ubuntu", "Debian"]
fake_copy = original

fake_copy.append("Arch")
print(f"Original: {original}")

print("\n--- 2.Shallow Copy ---")
sys_list = ["CPU", "RAM"]
real_copy = sys_list.copy()
real_copy.append("GPU")
print(f"Original: {sys_list} | copy: {real_copy}") #Safe!

print("\n--- 3. Deep Copy (The Nested List Problems) ---")
# A list conataining anothe list
config = ["Network",["IP: 10.0.0.1", "Port: 80"]]

shallow = config.copy()
deep = copy.deepcopy(config)

#if we change the Nested list inside the shallow copy...
shallow[1][1] = "Port: 443"

print(f"Original config port: {config[1][1]}") # It changed the original!
print(f"Deep copy port: {deep[1][1]}")          # Deep copy remained safe!