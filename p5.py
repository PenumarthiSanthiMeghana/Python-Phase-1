class car:
    maxspeed=20
    name=""
    def __init__(self):
        self.maxspeed=200
        self.name="supercar"
    def drive(self):
        print(self.maxspeed)
car1=car()
car1.drive()
car1.maxspeed=10
car1.drive()