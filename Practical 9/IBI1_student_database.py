class students(object):
    """
    Includes students name, major (BMI/BMS), score for their code portfolio, score for their group project, and exam score. All scores should be marks out of 100.
    """
    def __init__(self, name, major, code_score, group_score, exam_score):
        self.name = name
        self.major = major
        self.code_score = code_score
        self.group_score = group_score
        self.exam_score = exam_score
    def Print(self):
        print(self.name, end = ', ')
        print(self.major, end = ', ')
        print(self.code_score, end = ', ')
        print(self.group_score, end = ', ')
        print(self.exam_score)
# Example
Zhu_Yichen = students("Zhu Yichen", "BMI", 100, 100, 100)
students.Print(Zhu_Yichen)