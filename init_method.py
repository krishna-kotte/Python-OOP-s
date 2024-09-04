class Student:
    # init is a special method [ like constructor]
    def __init__(self,name,roll_no,age):
        self.name= name
        self.roll_no = roll_no
        self.age = age

    def stu_details(self):
        print("Student name is",self.name)
        print("Student roll no is",self.roll_no)
        print("Student age is",self.age)

obj_Student = Student("krishna",27,18)

obj_Student.stu_details()

