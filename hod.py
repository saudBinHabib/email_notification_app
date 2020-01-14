from person import Person


class HOD(Person):

    def __init__(self, fname, lname, email, teachers=None):
        super().__init__(fname, lname, email)
        self.department = None
        self.teachers = teachers if teachers else []

    def __repr__(self):
        return ' HOD: {}, {}, {}, {}'.format(self.fname, self.lname, self.email, self.department)

    def set_department(self, department):
        self.department = department

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
