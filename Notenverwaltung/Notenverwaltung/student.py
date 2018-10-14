
class Student:
    """A sample Employee class"""

    def __init__(self, vorname, nachname, matrnr):
        self.vorname = vorname
        self.nachname = nachname
        self.matrnr = matrnr
        # self.note = note

    # @property
    # def email(self):
    #     return '{}.{}@email.com'.format(self.vorname, self.nachname)
    #
    # @property
    # def fullname(self):
    #     return '{} {}'.format(self.vorname, self.nachname)
    #
    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.vorname, self.nachname, self.matrnr)