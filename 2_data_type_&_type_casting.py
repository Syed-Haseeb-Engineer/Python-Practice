#%%
ram_gb = 16
kernel_version = 6.8
distro_name = "Ubuntu"

print(f"ram_gb is {ram_gb} | Type: {type(ram_gb)}")
print(f"kernel_version {kernel_version} | Type: {type(kernel_version)}")
print(f"distro_name {distro_name} | Type: {type(distro_name)}")


simulated_file_input = "500"

clean_number = int(simulated_file_input)
print(f"\nCasted to integer: {clean_number} | New Type: {type(clean_number)}")

print(f"Math works now: {clean_number + 50}")

precise_number = float(clean_number)
print(f"casted to float: {precise_number} | New Type: {type(precise_number)}")

version_text = str(kernel_version)
print(f"Casted back to string: '{version_text}' | New Type: {type(version_text)}")