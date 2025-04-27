from abc import ABC, abstractmethod
class Animal(ABC):
    def print_info(self, name):
        print("Animal name:", name )


    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")


dog_obj = Dog()
dog_obj.make_sound()
dog_obj.print_info("Buddy")