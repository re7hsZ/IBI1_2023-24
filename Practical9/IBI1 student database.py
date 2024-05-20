# Pseudocode:
# Define a class named 'students' that inherits from the 'object' class.
# The class should have an initializer method '__init__' that takes the following parameters:
# - 'name': the name of the student,
# - 'major': the major of the student (either BMI or BMS),
# - 'code_score': the score for the student's code portfolio out of 100,
# - 'group_score': the score for the student's group project out of 100,
# - 'exam_score': the student's exam score out of 100.
# These parameters are used to create instance variables for each student.
# Define a method 'Print' within the class that prints all the details of a student in a single line.
# The 'Print' method should not return any value; it should only output the student's details.

class students(object):
    """
    A class to represent a student with attributes for name, major, and scores.
    """

    def __init__(self, name, major, code_score, group_score, exam_score):
        """
        Initialize a new student instance with name, major, and scores.

        Parameters:
        name (str): The name of the student.
        major (str): The major of the student, either 'BMI' or 'BMS'.
        code_score (int): The score of the student for their code portfolio out of 100.
        group_score (int): The score of the student for their group project out of 100.
        exam_score (int): The student's exam score out of 100.
        """
        self.name = name
        self.major = major
        self.code_score = code_score
        self.group_score = group_score
        self.exam_score = exam_score

    def Print(self):
        """
        Print the student's details in a single line.
        """
        print(self.name, end=', ')
        print(self.major, end=', ')
        print(self.code_score, end=', ')
        print(self.group_score, end=', ')
        print(self.exam_score)

# Example usage of the class:
# Create an instance of the 'students' class with details for Zhang Haosheng
student1 = students("Zhang Haosheng", "BMI", 100, 100, 100)

# Call the 'Print' method on the instance to print the student's details
student1.Print()
