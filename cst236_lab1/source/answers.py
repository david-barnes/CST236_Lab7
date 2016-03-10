""" Source file for question answers """

from math import factorial, sqrt, sin, radians
from decimal import Decimal, getcontext
from datetime import date
from source.shape_checker import get_quadrilateral_corners_type


def fibonacci(num):
    """ function for generating a fibonacci sequence and returning the nth digit of it """
    num = int(num)
    fib_num = "0"
    last_num = 0
    if num > 1:
        cur_num = 1
        while len(fib_num) < num:
            temp = cur_num
            cur_num = last_num + temp
            last_num = temp
            fib_num += str(temp)
    return fib_num[num-1]


def calc_pi(num):
    """ calculates pi to num places and returns the last digit """
    num = int(num)
    getcontext().prec = num+1
    temp = Decimal(0)
    pie = Decimal(0)
    deno = Decimal(0)
    k = 0

    for k in range(num):
        temp = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pie += Decimal(temp)/Decimal(deno)
    pie = pie * Decimal(12)/Decimal(640320**Decimal(1.5))
    pie = 1/pie
    pie_str = str(pie)
    if num == 1:
        return pie_str[0]
    else:
        return pie_str[num]



def conversion(value, unit_from, unit_to):
    """ converts the input value to the specified units """
    conversion_factors = {"inches":39.3701, "feet":3.28081, "yards":1.09361,
                          "miles":0.000621371, "nanometers":1000000000,
                          "micrometers":1000000, "millimeters":1000,
                          "centimeters":100, "meters":1, "kilometers":0.001}
    value = float(value)
    units = (value/conversion_factors[unit_from]) * conversion_factors[unit_to]
    return str(units)+' '+unit_to


def can_convert():
    """ prints out the conversion_factors dict """
    conversion_factors = {"inches":39.3701, "feet":3.28081, "yards":1.09361,
                          "miles":0.000621371, "nanometers":1000000000,
                          "micrometers":1000000, "millimeters":1000,
                          "centimeters":100, "meters":1, "kilometers":0.001}
    statement = "You may convert to/from the following units: "
    for key in conversion_factors.keys():
        statement += key
        statement += ', '
    return statement


def i_know():
    """ prints out all the questions the program knows """
    from source.main import Interface
    known = Interface()
    statement = "I know the following things: "
    for key in known.question_answers.keys():
        statement += key
        statement += '? '
    return statement


def get_triangle_area(side_a=0, side_b=0, dummy=0):
    """ calculates and returns the area of the given triangle """
    base = side_a/2
    temp = (side_b*side_b) - (base*base)
    height = sqrt(temp)
    area = (side_a * height) / 2
    return str(area)

#pylint: disable=too-many-arguments
# function requires 8 arguments
def get_quadrilateral_area(side_a=0, side_b=0, side_c=0, side_d=0,
                           corner_ab=0, corner_bc=0, corner_cd=0, corner_ad=0):
    """ calculates and returns the area of the given quadrilateral """
    result = get_quadrilateral_corners_type(side_a, side_b, side_c, side_d,
                                                 corner_ab, corner_bc, corner_cd, corner_ad)
    if result == "square" or result == "rectangle":
        area = side_a * side_b
    elif result == "rhombus":
        getcontext().prec = 5
        area = (Decimal(side_a) * Decimal(side_b)) * Decimal(sin(radians(corner_ab)))
    else:
        return "Can not determine area because the quadrilateral is "+result
    return str(area)


def calculate_tip(tip, bill):
    """ calculates the tip """
    getcontext().prec = 3
    tip_percent = Decimal(tip)/100
    tip = Decimal(bill) * tip_percent
    return str(tip)


def calculate_sales_tax(sale, tax):
    """ calculates the total bill after tax """
    getcontext().prec = 4
    tax_percent = (Decimal(tax)/100) + Decimal(1)
    total = Decimal(sale) * tax_percent
    return str(total)


def days_to_christmas():
    """ determines how many day until christmas """
    date1 = date.today()
    date2 = date(2016, 12, 25)
    timedelta = date2 - date1
    return str(timedelta.days)
