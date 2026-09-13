def grade(avg):
    if avg >= 90: return 'A+'
    if avg >= 80: return 'A'
    if avg >= 70: return 'B'
    if avg >= 60: return 'C'
    if avg >= 50: return 'D'
    return 'F'

assert grade(90) == 'A+'
assert grade(80) == 'A'
assert grade(70) == 'B'
assert grade(59.99) == 'D'
assert grade(49.99) == 'F'
print("Grade boundary tests passed")
