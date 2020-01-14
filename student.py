from person import Person


class Student(Person):

    def __init__(self, fname, lname, email, department, teachers=None):
        super().__init__(fname, lname, email)
        self.department = department
        self.teachers = teachers if teachers else []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def __repr__(self):
        return 'Student:{}, {}, {}, {}, {}'.format(self.fname, self.lname, self.email, self.full_name, self.department)
