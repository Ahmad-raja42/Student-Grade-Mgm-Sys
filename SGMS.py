# Function to calculate total score and grade
def calculate_total_and_grade(scores):
    total = sum(scores)
    average = total / len(scores)
    
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    return total, grade

# Function to display student details
def display_student_details(students):
    print("\n--- Student Details ---")
    for student in students:
        print(f"Name: {student['name']}, ID: {student['id']}, Total Score: {student['total_score']}, Grade: {student['grade']}")

# List to store student data
students = []

# Input loop for multiple students
while True:
    name = input("Enter student's name: ")
    student_id = input("Enter student's ID: ")
    
    # Taking input for scores in 3 subjects
    scores = []
    for i in range(5):
        score = int(input(f"Enter score for subject {i+1}: "))
        scores.append(score)
    
    # Calculate total score and grade
    total_score, grade = calculate_total_and_grade(scores)
    
    # Store student details in a dictionary
    student = {
        'name': name,
        'id': student_id,
        'scores': scores,
        'total_score': total_score,
        'grade': grade
    }
    
    # Add student to the list
    students.append(student)
    
    # Option to add another student or stop
    more_students = input("Do you want to add another student? (yes/no): ").lower()
    if more_students != 'yes':
        break

# Display all student details
display_student_details(students)