class Student:
    def __init__(self, name, roll_number, initial_grade):
        self.name = name
        self.roll_number = roll_number
        self.__grades = []  # Private list for grades
        
        # Add the first grade silently (without printing)
        if 0 <= initial_grade <= 100:
            self.__grades.append(initial_grade)

    def add_grade(self, grade):
        """Adds a grade if it's valid, else prints an error."""
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added.")
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

    def get_average_grade(self):
        """Returns the average grade of the student."""
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0

    def display_info(self):
        """Displays student's name and roll number."""
        print(f"Student Name: {self.name}, Roll Number: {self.roll_number}")

# Taking input
name = input().strip()
roll_number = input().strip()
initial_grade = int(input().strip())  # First grade input

# Creating the student object
student = Student(name, roll_number, initial_grade)
student.display_info()  # Display student info first

# Taking additional grades
while True:
    try:
        grade = int(input().strip())
        student.add_grade(grade)
    except:
        break  # Stop when no more input

# Printing the final average grade
print(f"Average Grade: {student.get_average_grade():.1f}")
