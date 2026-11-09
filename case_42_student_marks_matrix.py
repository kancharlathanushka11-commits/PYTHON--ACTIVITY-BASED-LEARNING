# Case 42: Student Marks Matrix Analysis

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Python", "Maths", "English"]

marks = [
    [85, 90, 80],
    [70, 75, 65],
    [95, 92, 88]
]

# Calculate each student's total and average
totals = []
print("STUDENT MARKS REPORT")
print("--------------------")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)
    print(students[i], "Total:", total, "Average:", round(average, 2))

# Calculate each subject's average
print("\nSUBJECT AVERAGES")

for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += marks[i][j]

    average = total / len(students)
    print(subjects[j], "Average:", round(average, 2))

    if average < 70:
        print("Low-performing subject:", subjects[j])

# Identify the top performer
top_index = totals.index(max(totals))
print("\nTop Performer:", students[top_index])
print("Highest Total Marks:", totals[top_index])
