# method for displaying a string like "You have a soda with such and such a taste" if the taste is set.
# If not specified, output the line "Just soda"
# task 1 class soda
class Soda:
    def __init__(self, taste_of_soda):
        self.taste_of_soda = taste_of_soda

    def taste(self):
        if self.taste_of_soda == "сherry":
            print(f"Soda with taste {self.taste_of_soda} !")
        elif self.taste_of_soda == " ":
            print("Just soda !")


action = Soda("сherry")
action.taste()

action2 = Soda(" ")
action2.taste()


# When passing parameters a and b to methods,
# you need to perform appropriate actions with them and print the response.
class Math(object):
    def __init__(self, math_list):
        self.math_list = math_list

    # Subtraction
    def __sub__(self, other):
        minuslst = []
        zipped = zip(self.math_list, other.math_list)
        for tup in zipped:
            minuslst.append(tup[0] - tup[1])
        return Math(minuslst)

    # Addition
    def __add__(self, other):
        addlst = [x + y for x, y in zip(self.math_list, other.math_list)]
        return Math(addlst)

    # Multiplication
    def __mul__(self, other):
        mullst = [x * y for x, y in zip(self.math_list, other.math_list)]
        return Math(mullst)

    # Division
    def __truediv__(self, other):
        devlst = [x / y for x, y in zip(self.math_list, other.math_list)]
        return Math(devlst)

    def __str__(self):
        return str(self.math_list)


a = Math([100])
b = Math([10])

p = a - b
z = a + b
q = a * b
w = a / b

print('Subtraction: ' + str(p))
print('Addition: ' + str(z))
print('Multiplication: ' + str(q))
print('Division' + str(w))


# program with the Car class
class Car:

    def __init__(self, starting_the_car, turning_off_the_car, year_of_release, type_of_car, car_color):
        self.starting_the_car = starting_the_car
        self.turning_off_the_car = turning_off_the_car
        self.year_of_release = year_of_release
        self.type_of_car = type_of_car
        self.car_color = car_color

    def starting(self):
        if self.starting_the_car == "start car":
            print("The car is started")
        if self.turning_off_the_car == "stop car":
            print("The car is turned off")
        if self.year_of_release == "year":
            print(f"The car was released in: {year} year")
        if self.type_of_car == "type_car":
            print(f"Сar type = {type_car}!")
        if self.car_color == "color":
            print(f"Color car = {color}")


color = "black"
type_car = "sedan"
year = "2010"

action = Car("start car", "stop car", "year", "type_car", "color")
action.starting()


# a sphere in three-dimensional space
from math import pi


class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            raise TypeError
        self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2


s0 = Sphere(0.5)  # test sphere creation with radius and default center
print(s0.get_center())  # (0.0, 0.0, 0.0)
print(s0.get_volume())  # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0))  # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))  # True
print(s0.get_radius())  # 1.6



# the SuperStr class, which inherits the functionality of
# the standard str type and contains 2 new methods
class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrome(s):
        string = s
        if string == string[::-1]:
            print("The letter is a palindrome")
        else:
            print("The letter is not a palindrome")


s = SuperStr('123123123123')
print(s.is_repeatance('13'))
# False
s.is_palindrome()
# The letter is not a palindrome


# calendar function
def create_calendar_page(m=8, y=2022):
    import calendar

    s = ''
    lin = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
    c = calendar.Calendar()


    for i in c.monthdayscalendar(y, m):
        for q in i:
            q = str(q)
            if q == '0': q = q.replace('0', '  ')
            if len(q) == 1: q = '0' + q
            s = s + q + ' '
        s = s + '\n'
    s = s.replace(' \n', '\n')
    return lin+s


print(create_calendar_page(1))
print(create_calendar_page(m=8, y=2022))