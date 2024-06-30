class car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self):
        print(self.__maxspeed)
car1=car()
car1.drive()
car1.__maxspeed=10
car1.drive()