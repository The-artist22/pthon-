# question no 1
# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# question no 2


# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# for student, score in student_scores.items():
#     print(f"Student: {student}, Score: {score}")

# questuion 3 

# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }


# total_scores = 0

# for score in student_scores.values():
#     total_sum += score


# average_score = total_scores / len(student_scores)

# print("The average score of the students is:", average_score)


# question 4


# student_scores = {
#     'Alice': 95,
#     'Bob': 82,
#     'Charlie': 78,
#     'David': 65,
#     'Eva': 88
# }


# student_grades = {}

# for student, score in student_scores.items():
#     if score >= 90:
#         student_grades[student] = 'A'
#     elif score >= 80:
#         student_grades[student] = 'B'
#     elif score >= 70:
#         student_grades[student] = 'C'
#     else:
#         student_grades[student] = 'D'

# print(student_grades)


# question 4

# student_scores = {
#     'Alice': 95,
#     'Bob': 82,
#     'Charlie': 78,
#     'David': 65,
#     'Eva': 88
# }


# for student in student_scores:
#     student_scores[student] += 5


# print(student_scores)

# question 5


# employee = {
#     "John": 55000,
#     "Emma": 60000,
#     "Harry": 70000,
#     "Sophia": 65000,
#     "Mike": 48000
# }


# print(employee)


 
#  quesstion 5 ka 1
# employee_data = {
#     "John": 55000,
#     "Emma": 60000,
#     "Harry": 70000,
#     "Sophia": 65000,
#     "Mike": 48000
# }


# for employee, salary in employee_data.items():
#     if salary > 60000:
#         print(employee)



# question 5 ka 2

# employee_data = {
#     "John": 55000,
#     "Emma": 60000,
#     "Harry": 70000,
#     "Sophia": 65000,
#     "Mike": 48000
# }

# for employee in employee_data:
#     employee_data[employee] *= 1.10  # Increase salary by 10%


# print(employee_data)

# question 6


# book_inventory = {
#     "The Great Gatsby": 5,
#     "1984": 8,
#     "To Kill a Mockingbird": 3,
#     "The Catcher in the Rye": 6,
#     "Moby-Dick": 4
# }


# for book in book_inventory:
#     book_inventory[book] += 2 


# print(book_inventory)


# question 7


# book_inventory = {
#     "The Great Gatsby": 5,
#     "1984": 8,
#     "To Kill a Mockingbird": 3,
#     "The Catcher in the Rye": 6,
#     "Moby-Dick": 4
# }


# total_books = 0


# for copies in book_inventory.values():
#     total_books += copies


# print("Total number of books in the library:", total_books)


# question 8

# book_list = [
#     {"name": "The Great Gatsby", "quantity": 4},
#     {"name": "1984", "quantity": 6},
#     {"name": "To Kill a Mockingbird", "quantity": 3},
#     {"name": "Moby Dick", "quantity": 2}
# ]


# for book in book_list:
#     if book["quantity"] >= 5:
#         book["stock"] = "Popular"
#     elif book["quantity"] >= 3:
#         book["stock"] = "Available"
#     else:
#         book["stock"] = "Limited"

# print(book)



# """
# Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}


# 1. display Alice English Score
# 2. display Bob Class
# 3. display Charlie Math Score
# 4. display Diana's avg score
# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
# 6. Add new Student and its subject, score and class in same dict i.e students
# 7. add new subject and its score in John
# """


print("Alice english score: ",students["Alice"]["Scores"][2])
print("Bob class: ",students["Bob"]["Class"])
print("Bob class: ",students["Bob"]["Class"])
print("Charlie Math Score:", students["Charlie"]["Scores"][0])
diana_avg_score = sum(students["Diana"]["Scores"]) / len(students["Diana"]["Scores"])
print("4. Diana's Average Score:", diana_avg_score)
print("5. John's Subjects and Scores:")
for subject, score in range(students["John"]["Subjects"], students["John"]["Scores"]):
    print(f"   Subject: {subject}, Score: {score}")
new_student = "Ahmed"
students[new_student] = {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [95, 88, 92],
    "Class": 10
}
print(f"Added {new_student} with Subjects, Scores, and Class:", students[new_student])
new_subject = "History"
new_score = 70
students["John"]["Subjects"]+=(new_subject)
students["John"]["Scores"]+=(new_score)
print(f"Added new subject {new_subject} with score {new_score} for John:", students["John"])
