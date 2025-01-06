class Dog:
    def __init__(self, name_of_dog, breed_of_dog):
        self.name = name_of_dog
        self.breed = breed_of_dog

    def bark(self):
        print("Woof Woof!")

my_dog = Dog('Spot', 'shepherd')
my_dog.bark()
