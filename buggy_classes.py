def main():
    class Person:
        def __init__(self, first_name, last_name):
            self.first = first_name
            self.last = last_name

        def speak(self):
            print("My name is " + self.first + " " + self.last)

    me = Person("Walter", "Abish")
    you = Person("Abiola", "Abrams")

    me.speak()
    you.speak()

main()