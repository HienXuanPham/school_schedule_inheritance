from school_schedule.student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        transportation_message = "gets transportation" if self.gets_transportation else "walks"
        return super().summary() + "\n" + f"{self.name} " + transportation_message + " to school."