class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine is started")


c = Car("BMW", 2017)
e = c.Engine(7)
e.start()
print(e.number)