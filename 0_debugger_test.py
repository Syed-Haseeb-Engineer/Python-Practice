def calculate_compund_interest(principal, rate, years):
    """Calculates interest over time to practice debugging."""
    current_amount = principal

    for year in range (1, years + 1):
        interest_gained = current_amount * rate
        current_amount += interest_gained

        print(f"Year {year}: Ubuntu server find is at ${current_amount:.2f}")
    return current_amount

final_balance = calculate_compund_interest(1000.0, 0.05, 3)
print(f"\nFinal Balance: ${final_balance:.2f}")

# import time
# print("Starting the sysmte check..")

# for i in range(1,4):
#     status = f"Cheecking core{i}.."
#     print(status)
#     time.sleep(0.5)

# print("System check complete!")