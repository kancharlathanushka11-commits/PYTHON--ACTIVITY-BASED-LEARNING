# Case 45: Weekly Electricity Consumption Matrix

appliances = ["Fan", "Light", "Computer"]

# Seven readings per appliance, in kWh
usage = [
    [1.2, 1.1, 1.3, 1.2, 1.1, 1.4, 1.0],
    [0.8, 0.7, 0.8, 0.9, 0.7, 0.8, 0.9],
    [2.5, 2.8, 3.0, 2.6, 2.9, 3.2, 2.7]
]

daily_limit = 5.0
appliance_totals = []

# Calculate weekly consumption for each appliance
for i in range(len(appliances)):
    total = sum(usage[i])
    appliance_totals.append(total)
    print(appliances[i], "weekly consumption:", round(total, 2), "kWh")

# Calculate daily consumption
for day in range(7):
    daily_total = 0

    for appliance in range(len(appliances)):
        daily_total += usage[appliance][day]

    print("Day", day + 1, "total:", round(daily_total, 2), "kWh")

    if daily_total > daily_limit:
        print("Warning: daily limit exceeded")

# Identify the appliance with the highest weekly consumption
highest = appliance_totals.index(max(appliance_totals))
print("Highest-consuming appliance:", appliances[highest])
