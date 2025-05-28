marksheets = {
    "Aman": {
        "subjects": {
            "Python Programming": 92,
            "Machine Learning": 88,
            "Data Structures": 94,
            "Database Systems": 89,
            "Cloud Computing": 91
        },
        "grade": "A+",
        "attendance": "97%"
    },
    "Vidhi": {
        "subjects": {
            "Python Programming": 85,
            "Machine Learning": 80,
            "Data Structures": 87,
            "Database Systems": 90,
            "Cloud Computing": 88
        },
        "grade": "A",
        "attendance": "93%"
    }
}

print(marksheets)

for i, j in marksheets.items():
    
    print(f"Student: {i}")

    print("Subjects and Marks:")
    
    for subject, marks in j["subjects"].items():
       
        print(f"{subject}: {marks}")
    
    print(f"Grade: {j['grade']}")
    
    print(f"Attendance: {j['attendance']}")
    
    print()