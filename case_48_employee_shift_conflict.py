# Case 48: Tuple-Based Employee Shift Conflict Detection

shifts = [
    ("Asha", 9, 12),
    ("Ravi", 10, 14),
    ("Asha", 11, 13),
    ("Asha", 13, 16),
    ("Ravi", 15, 17)
]

conflict_found = False

for i in range(len(shifts)):
    name1, start1, end1 = shifts[i]

    for j in range(i + 1, len(shifts)):
        name2, start2, end2 = shifts[j]

        if name1 == name2 and start1 < end2 and start2 < end1:
            print("Conflict:", shifts[i], "and", shifts[j])
            conflict_found = True

if not conflict_found:
    print("No shift conflicts found.")
