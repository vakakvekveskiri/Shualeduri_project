import math


def circle_area(pi):
    def whole_area(radius):
        return pi *  radius ** 2
    return whole_area

func = circle_area(math.pi)
print(func(3))