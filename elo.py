K = 20

def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def update_elo(rating_a, rating_b, score_a):
    exp_a = expected_score(rating_a, rating_b)

    new_a = rating_a + K * (score_a - exp_a)
    new_b = rating_b + K * ((1 - score_a) - (1 - exp_a))

    return new_a, new_b
