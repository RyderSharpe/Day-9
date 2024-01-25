# {"Key": "Value"}

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    #print(student) # prints Harry
    grade = (student_scores[student]) # prints value, ie 81

    if 91 <= grade <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= grade <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= grade <= 80:
        student_grades[student] = "Acceptable"
    elif grade <= 70:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
