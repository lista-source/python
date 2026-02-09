class Person:
    def speak(self):
        print("I am a Kikuyu")
class Chebet(Person):
    def speak(self):
        print("I am a Kalenjin")
class Naserian(Person):
    def speak(self):
        print("I am a Maasai")
naserian1 = Naserian()
naserian1.speak()
chebet1 = Chebet()
chebet1.speak()