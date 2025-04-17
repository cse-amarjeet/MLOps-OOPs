# class Animal:
#     def __init__(self):
#         self.name = "Buddy"
        
#     def speak(self):
#         print(f"{self.name} makes sound")
    

# class Dog(Animal):
#     def __init__(self,bread):
#         super().__init__()
#         self.bread = bread
    
#     def speak(self):
#         super().speak()
#         print(f"{self.name} bark, It is a {self.bread}")


# dog = Dog("Golden Retriver")
# dog.speak()
    

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.

