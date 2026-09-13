def average(values):
    return sum(values) / len(values) if values else 0

assert average([]) == 0
assert average([60, 80, 100]) == 80
assert average([75]) == 75
print('Performance average rules passed')
