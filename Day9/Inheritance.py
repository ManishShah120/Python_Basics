#INheritance is a method of reusing code
class Mammal:#This are Class
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()#This are object
dog1.bark()

cat1 = Cat()
cat1.be_annoying()