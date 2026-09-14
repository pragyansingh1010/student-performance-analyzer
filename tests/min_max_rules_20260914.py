def bounds(values):
    return min(values), max(values)

assert bounds([40, 80, 60]) == (40, 80)
assert bounds([75]) == (75, 75)
assert bounds([0, 100]) == (0, 100)
print('Performance min/max rules passed')
