class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")


animal = Animal()
animal.make_sound()  

cat = Cat()
cat.make_sound()  

