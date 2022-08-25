"""
What is 'Inheritance'?
    - 서로 다른 클래스에서, 중복된 메소드를 써야 할 때 부모 클래스에서 상속받아 사용
    - method overriding : 부모 메소드 덮어쓰기 
"""

class Person:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def getName(self):
        print("Name: {}".format(self.name))

    def getAge(self):
        print("Age: {}".format(self.age))

    def getStatus(self):
        print("Status: {}".format(self.status))

class Student(Person):
    def __init__(self, name, age, status, school, GPA):
        super().__init__(name, age, status)
        self.school = school
        self.GPA = GPA
    
    def getSchool(self):
        print("School: {}".format(self.school))

    def getGPA(self):
        print("GPA: {}".format(self.GPA))


st1 = Student("정환희", 21, "happy", "연세대학교", 4.06)
st1.getName()
st1.getAge()
st1.getSchool()
st1.getGPA()