# Case 44: Hospital Ward Occupancy Monitoring

wards = ["Ward A", "Ward B", "Ward C"]
capacities = [30, 20, 25]
days = ["Mon", "Tue", "Wed"]

occupancy = [
    [25, 29, 31],
    [15, 18, 17],
    [20, 22, 24]
]

daily_totals = [0] * len(days)

for i in range(len(wards)):
    for j in range(len(days)):
        occupied = occupancy[i][j]
        daily_totals[j] += occupied

        utilization = occupied / capacities[i] * 100

        print(
            wards[i], days[j],
            "Utilization:", round(utilization, 1), "%"
        )

        if occupied > capacities[i]:
            print("CAPACITY VIOLATION:", wards[i], days[j])

peak_index = daily_totals.index(max(daily_totals))

print("Daily Totals:", daily_totals)
print("Peak-Demand Day:", days[peak_index])
