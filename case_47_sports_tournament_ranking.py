# Case 47: Sports Tournament Ranking System

teams = ["Tigers", "Eagles", "Lions"]

# Match format: (team1, score1, team2, score2)
matches = [
    ("Tigers", 3, "Eagles", 1),
    ("Lions", 2, "Tigers", 2),
    ("Eagles", 2, "Lions", 0)
]

# Initialize team statistics
stats = {}

for team in teams:
    stats[team] = {"points": 0, "for": 0, "against": 0}

# Process match results
for t1, s1, t2, s2 in matches:
    stats[t1]["for"] += s1
    stats[t1]["against"] += s2

    stats[t2]["for"] += s2
    stats[t2]["against"] += s1

    if s1 > s2:
        stats[t1]["points"] += 3
    elif s2 > s1:
        stats[t2]["points"] += 3
    else:
        stats[t1]["points"] += 1
        stats[t2]["points"] += 1

# Rank teams by points and score difference
ranking = sorted(
    teams,
    key=lambda team: (
        stats[team]["points"],
        stats[team]["for"] - stats[team]["against"]
    ),
    reverse=True
)

# Display tournament ranking
print("Rank Team       Points Difference")

for rank, team in enumerate(ranking, start=1):
    difference = stats[team]["for"] - stats[team]["against"]
    print(rank, team, stats[team]["points"], difference)
