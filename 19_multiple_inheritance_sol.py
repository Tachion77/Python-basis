class Teacher:
    def action_teacher(self):
        print("I am teacher")

class Engineer:
    def action_engineer(self):
        print("I am engineer")

class Youtuber:
    def action_youtuber(self):
        print("I am youtuber")

class Person(Teacher, Engineer, Youtuber):
    pass

me = Person()
me.action_teacher()
me.action_engineer()
me.action_youtuber()