students = {
    "Jainish": 85,
    "Aarav": 92,
    "Isha": 78,
    "Meera": 92,
    "Rahul": 67
}

max_score = max(students.values())

topper = [name for name,score in students.items() if score == max_score]

print("max score = ", max_score)
print("Topper(s):", topper)