class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,student_id,grade):
        super().__init__(name, age)
        self.student_id=student_id
        self.grade=grade
    
    def display_profile(self):
        print("Student Profile")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Student ID : {self.student_id}")
        print(f"Grade      : {self.grade}")
    
s = Student("Zain", 20, "S123", "A")
s.display_profile()        