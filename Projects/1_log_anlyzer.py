raw_log = "ERROR: disk_space_full; WARNING: high_cpu; ERROR: network_timeout"

#slippting by ';' 
alerts = raw_log.split(";")

issues_list = [alert.split(": ")[1] for alert in alerts]
print(f"Extracted List: {issues_list}")

unique_issues = set(issues_list)
print(f"Unique Set: {unique_issues}")


issues_lenghts = {issue: len(issue) for issue in unique_issues}

print("\n--- Final Analysis ---")
for issue, length in issues_lenghts.items():
    print(f"Issue: '{issue}' | Char Length: {length}")