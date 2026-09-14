def total(values):
    return sum(values)

assert total([]) == 0
assert total([25, 25, 50]) == 100
assert total([100]) == 100
print('Performance total rules passed')
