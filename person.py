class Person:

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    @property
    def full_name(self):
        return '{0} {1}'.format(self.fname, self.lname)
