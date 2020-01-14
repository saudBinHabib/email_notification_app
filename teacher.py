from person import Person


class Teacher(Person):

    def __init__(self, fname, lname, email, students=None):
        super().__init__(fname, lname, email)
        self.students = students if students else []
        self.department = None
        self.HOD = None

    def __repr__(self):
        return ' Teacher : {}, {}, {}, {}, {}'.format(self.fname, self.lname, self.email, self.department, self.HOD)

    def set_department(self, department):
        self.department = department

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def set_HOD(self, hod):
        self.HOD = hod
