class Animal:

    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Animal sound")
    
class Dog(Animal):

    def __init__(self):
        super().__init__("home")

    def sound(self):
        print("wof wof")

d = Dog()
print(d.habitat)
d.print_habitat()
d.sound()
