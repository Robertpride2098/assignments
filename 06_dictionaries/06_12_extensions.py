# Extend a dictionary with additional course information and present the updated information in a readable format.
# Honestly had no clue what to do for this one, so i just made a dictionary with some courses and added some more information to it
# also used the ai  
# difficulty rating of 9/10
courses = {
    "2024-01": {
        "title": "Introduction to Python",
        "instructor": "Ms. Rivera",
        "room": "Lab 2",
        "students": 18,
        "status": "In progress",
    },
    "2024-02": {
        "title": "Data Structures",
        "instructor": "Mr. Chen",
        "room": "Room 104",
        "students": 24,
        "status": "Scheduled",
    },
}

# Add a new course and extend an existing course with more details.
courses["2024-03"] = {
    "title": "Web Applications",
    "instructor": "Dr. Patel",
    "room": "Lab 4",
    "students": 20,
    "status": "Scheduled",
}
courses["2024-01"]["level"] = "Beginner"
courses["2024-01"]["next_class"] = "Tuesday, 10:00 AM"

print("Course schedule")
print("================")
for code, course in courses.items():
    print(f"{code}: {course['title']}")
    print(f"  Instructor: {course['instructor']}")
    print(f"  Room: {course['room']}")
    print(f"  Students: {course['students']}")
    print(f"  Status: {course['status']}")
    if "level" in course:
        print(f"  Level: {course['level']}")
    if "next_class" in course:
        print(f"  Next class: {course['next_class']}")
    print()
