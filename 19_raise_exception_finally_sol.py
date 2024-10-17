class AdulException(Exception):
    pass

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_minor_age(self):
        if int(self.age) >= 18:
            raise AdulException
        else:
            return self.age
    
    def display(self):
        try:
            print(f"age of the person is: {self.get_minor_age()}")
        except AdulException:
            print(f"Person is adult. Age: {self.age}")
        finally:
            print(f"name of this person is: {self.name}")

Person("Marcel", 20).display()
Person("Marcel", 17).display()

