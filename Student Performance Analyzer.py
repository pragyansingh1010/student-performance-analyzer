import pandas as pd
import numpy as np

data = {
    'Name': ['Aman', 'Rahul', 'Priya', 'Neha', 'Karan', 'Simran', 'Arjun', 'Riya'],
    'Python': [85, 72, 91, 68, 78, 95, 60, 88],
    'Java': [78, 80, 89, 65, 75, 92, 55, 84],
    'Maths': [90, 76, 94, 70, 82, 88, 62, 91],
    'AI': [88, 75, 92, 72, 80, 96, 58, 89]
}

df = pd.DataFrame(data)

subjects = ['Python', 'Java', 'Maths', 'AI']

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)

def grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(grade)

df['Result'] = np.where(
    (df[subjects] >= 40).all(axis=1),
    'Pass',
    'Fail'
)

print(df.to_string(index=False))

class_average = df[subjects].mean().mean()
print("\nClass Average:", round(class_average, 2))

top3 = df.sort_values('Average', ascending=False).head(3)
print("\nTop 3 Students:")
print(top3[['Name', 'Total', 'Average', 'Grade']].to_string(index=False))

print("\nSubject-wise Average:")
print(df[subjects].mean().round(2))

print("\nSubject Highest Marks:")
for subject in subjects:
    print(subject, ":", df[subject].max())

print("\nSubject Lowest Marks:")
for subject in subjects:
    print(subject, ":", df[subject].min())

print("\nNumber of Students in Each Grade:")
print(df['Grade'].value_counts().sort_index())