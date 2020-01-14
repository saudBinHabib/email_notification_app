class Department:

    def __init__(self, name, teachers=None, students=None):
        self.name = name
        self.HOD = None
        self.teachers = teachers if teachers else []
        self.students = students if students else []

    def set_HOD(self, hod):
        self.HOD = hod

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)