class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Hello, my name is", self.name, "and my age is", self.age)

Kornel = Cat("Kornél", 7)
Kornel.speak()
