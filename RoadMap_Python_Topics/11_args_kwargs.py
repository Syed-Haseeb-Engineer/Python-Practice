def configure_server(hostname, *args, **kwargs):
    print(f"\nConfigurig Host: {hostname}")

    # *args is a tuple
    if args: 
        print("Executing setup commands:")
        for index, cmd in enumerate(args):
            print(f"Step {index + 1}: {cmd}")

    # **kwargs is a Dictionary
    if kwargs:
        print("Applying configuration rules:")
        for key, value in kwargs.items():
            print(f" {key.upper()}= {value}")


# We can pass as many or as few arguments as we want!
configure_server("web-01")

configure_server("db-01", "apt update", "systemctl restart postresql", port=5432, max_connections=100, firewall= "active")