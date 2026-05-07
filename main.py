import pandas as pd

K = 20
START = 1500

def expected(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))

def update(r_a, r_b, score_a):
    exp = expected(r_a, r_b)
    new_a = r_a + K * (score_a - exp)
    new_b = r_b + K * ((1 - score_a) - (1 - exp))
    return new_a, new_b

# 🔗 YOUR GOOGLE SHEET CSV LINK (paste yours here)
url = "https://docs.google.com/spreadsheets/d/1kfYGG1ScfNowyKskgaSACyV4Bhy-TCmyAAvGB6SPNSs/export?format=csv"

df = pd.read_csv(url)

ratings = {}

def get(team):
    if team not in ratings:
        ratings[team] = START
    return ratings[team]

for _, row in df.iterrows():
    a = row["team_a"]
    b = row["team_b"]
    ga = int(row["goals_a"])
    gb = int(row["goals_b"])

    if ga > gb:
        score_a = 1
    elif ga < gb:
        score_a = 0
    else:
        score_a = 0.5

    r_a = get(a)
    r_b = get(b)

    new_a, new_b = update(r_a, r_b, score_a)

    ratings[a] = new_a
    ratings[b] = new_b

print("\n🏆 Elo Ratings:\n")

for team, rating in sorted(ratings.items(), key=lambda x: -x[1]):
    print(team, round(rating, 2))
