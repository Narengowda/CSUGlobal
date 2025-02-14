course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}
course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

while True:
    course_number = input("enter a course number: ")
    if course_number in course_rooms:
        print(f"Course: {course_number}")
        print(f"Room: {course_rooms[course_number]}")
        print(f"Instructor: {course_instructors[course_number]}")
        print(f"Meeting Time: {course_times[course_number]}")
    else:
        print("Invalid course number.")