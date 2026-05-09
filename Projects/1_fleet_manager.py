def analyze_servers(servers):
    """
    Analyze server metrics using comprehensions and lambdas.
    Args:
        server (list): A list of dictionaries containing server data.
        
    Returns:
        tuple: A tuple containing all analysis results.
    """
    critican_names = [srv["name"] for srv in servers if srv["cpu"] > 80.0]

    unique_os = {srv["os"] for srv in servers}

    status_map = {srv["name"]: "WARN" if srv["cpu"] > 80.0 else "OK" for srv in servers}

    highest_cpu_server = max(servers, key=lambda s: s["cpu"])


    return critican_names, unique_os, status_map, highest_cpu_server

active_fleet = []
is_running = True

print("=== Ubuntu Fleet Manager CLI ====")

while is_running:
    print("\nOptions: [1] Add Server [2] Analyze Fleet [3] Exit")

    user_choice = input("Enter your choice (1/2/3)")

    if user_choice == "1":
        srv_name = input("Enter server hostname (e.g., web-01):")
        srv_os = input("Enter OS (e.g., Ubuntu 22.04):")
        cpu_input = input("Enter current CPU load % (e.g., 45.5):")

        try: 
            cpu_load = float(cpu_input)

            new_server = {"name": srv_name, "os": srv_os, "cpu": cpu_load}
            active_fleet.append(new_server)
            print(f"Success: {srv_name} added to fleet.")
        except ValueError:
            print("Error: CPU load must be a valid number! Please try again.")
            
    elif user_choice == "2":
        if not active_fleet:
            print("Error: Fleet is empty. Please add a server first.")
        else:
            crits, os_sets, statuses, highest = analyze_servers(active_fleet)

            print("\n--- Fleet Analysis Report ---")
            print(f"Critical Servers (CPU > 80%): {crits}")
            print(f"Unique Operating Systems: {os_sets}")
            print(f"Fleet Status Map: {statuses}")
            print(f"Highes Load: {highest['name']} at {highest['cpu']}%")
        
    elif user_choice == "3":
        print("Shutting down Fleet Manager. Goodbye!")
        is_running = False

    else:
        print("Invalid choice. Please enter 1,2, or 3.")

            