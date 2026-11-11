class Persion():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Persion):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        super(Student, self).info()
        print(self.name, self.age, "输出学号", self.stu_no)


class Teacher(Persion):
    def __init__(self, name, age, teachyear):
        super().__init__(name, age)
        self.teachyear = teachyear

    def info(self):
        super().info()  # python3的写法
        super(Teacher, self).info()  # python2的写法
        print(self.name, self.age, "教龄", self.teachyear)


stu = Student('张三', 20, 3333)
teacher = Teacher('李四', 33, 22)

stu.info()
teacher.info()
