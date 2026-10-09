# Parent class (Base class)
class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
    
    # Method overriding
    def make_sound(self):
        print(f"{self.name} barks: Woof!")
    
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

# Usage
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.eat()        # Inherited method
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method
#overridding method uses the same method name as parent class as a child class
#overloading method uses the same name method BUT different parameters
#this code is about inheritance from the parent class (ANIMAL)
#SUPER() means using parent constructor
"""expected results
max is eating
max barks: woof!
max is fetching the ball
whiskers meows: Meow!
whiskers is climbing a tree"""