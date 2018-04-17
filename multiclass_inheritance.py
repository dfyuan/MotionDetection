class Animal(object):
    def __init__(self,animal,*args):
        super(Animal, self).__init__(*args)
        print("init " + animal)

class GoodBoy(object):
    def __init__(self,goodboy,*args):
        super(GoodBoy, self).__init__(*args)
        print("init " + goodboy )

class Dog(object):
    def __init__(self,dog,*args):
        super(Dog, self).__init__(*args)
        for x in dog:
            print("init " + str(x))

class GermanShepard(Dog,GoodBoy,Animal):
    def __init__(self):
        print("init GermanShepard")
        super(GermanShepard,self).__init__({"Dog","trr"},"GoodBoy","Animal")

if __name__ == '__main__':
    gsd = GermanShepard()