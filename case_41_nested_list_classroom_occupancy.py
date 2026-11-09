# Case 41: Nested List Classroom Occupancy Analysis

classrooms = [
    ["S101", "S102", None, "S104"],
    ["S105", "S106", "S101", None],
    ["Reserved", "S108", None, "S110"]
]

reserved_seats = 1
assigned_students = []
duplicates = []
occupied_seats = 0
total_seats = 0

for classroom in classrooms:
    for seat in classroom:
        total_seats += 1

        if seat == "Reserved":
            continue
        elif seat is not None:
            if seat in assigned_students:
                duplicates.append(seat)
            else:
                assigned_students.append(seat)
                occupied_seats += 1

vacant_seats = total_seats - occupied_seats - reserved_seats

print("CLASSROOM OCCUPANCY REPORT")
print("--------------------------")
print("Total Seats:", total_seats)
print("Occupied Seats:", occupied_seats)
print("Reserved Seats:", reserved_seats)
print("Vacant Seats:", vacant_seats)
print("Duplicate Student Assignments:", duplicates)
