def score(correct, total):
    return correct / total * 100 if total else 0

assert score(5, 10) == 50
assert score(10, 10) == 100
