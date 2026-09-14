def valid_score(x):
    return 0 <= x <= 100

assert valid_score(0)
assert valid_score(100)
assert not valid_score(-1)
assert not valid_score(101)
print('Score validation passed')
