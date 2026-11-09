# Case 50: Tuple-Based Route Distance Analysis

from math import sqrt

points = [
    (0, 0),
    (3, 4),
    (9, 4),
    (10, 12)
]

longest_distance = -1
longest_segment = None

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    dx = x2 - x1
    dy = y2 - y1

    distance = sqrt(dx ** 2 + dy ** 2)

    print(
        "Segment", points[i], "to", points[i + 1],
        "distance:", round(distance, 2)
    )

    if distance > longest_distance:
        longest_distance = distance
        longest_segment = (points[i], points[i + 1])

print("Longest segment:", longest_segment)
print("Longest distance:", round(longest_distance, 2))
