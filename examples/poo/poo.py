class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

    def __dict__(self):
        return dict([('max',self.__maxspeed),("name",self.__name)] )

"""
Bloco principal da aplicação
"""
if __name__ == '__main__':
    redcar = Car()
    redcar.drive()
    redcar.__maxspeed = 10  # will not change variable because its private
    redcar.drive()
    redcar.setMaxSpeed(320)
    redcar.drive()
    print(redcar.__dict__())
