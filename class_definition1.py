#! /usr/bin/python3.8

class myclass:
    x = 200
    def f(self):
        return self.x





y = myclass()


print(y.f())


class complex:
    def __init__(self , real , img):
        self.x = real
        self.y = img

        print(self.x , self.y)


