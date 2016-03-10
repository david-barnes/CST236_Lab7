"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of
3 sides of a triangle is equilateral, scalene or isosceles
"""
# pylint: disable=no-member
# if the input is a dict, list, or tuple it would have those members
# pylint: disable=too-many-arguments
# when you have a quadrilateral with corners it will have 8 arguments
# pylint: disable=too-many-boolean-expressions
# first pylint can't count, and second all those boolean expressions
# are needed in those statements as there are at most 8 variables to compare
def get_triangle_type(side_a=0, side_b=0, side_c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param side_a: line a
    :type side_a: float or int or tuple or list or dict

    :param side_b: line b
    :type side_b: float

    :param side_c: line c
    :type side_c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(side_a, (tuple, list)) and len(side_a) == 3:
        side_c = side_a[2]
        side_b = side_a[1]
        side_a = side_a[0]

    if isinstance(side_a, dict) and len(side_a.keys()) == 3:
        values = []
        for value in side_a.values():
            values.append(value)
        side_a = values[0]
        side_b = values[1]
        side_c = values[2]

    if not (isinstance(side_a, (int, float)) and isinstance(side_b, (int, float))
            and isinstance(side_c, (int, float))):
        return "invalid"

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "invalid"

    if side_a == side_b and side_b == side_c:
        return "equilateral"

    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "isosceles"
    else:
        return "scalene"


def get_quadrilateral_type(side_a=0, side_b=0, side_c=0, side_d=0):
    """
    Determine if the given Quadrilateral is a rectangle or a square

    :param side_a: line a
    :type side_a: float or int or tuple or list or dict

    :param side_b: line b
    :type side_b: float

    :param side_c: line c
    :type side_c: float

    :param side_d: line d
    :type side_d: float

    :return: "rectangle", "square", or "invalid"
    :rtype: str
    """
    if isinstance(side_a, (tuple, list)) and len(side_a) == 4:
        side_d = side_a[3]
        side_c = side_a[2]
        side_b = side_a[1]
        side_a = side_a[0]

    if isinstance(side_a, dict) and len(side_a.keys()) == 4:
        values = []
        for value in side_a.values():
            values.append(value)
        side_a = values[0]
        side_b = values[1]
        side_c = values[2]
        side_d = values[3]

    if not (isinstance(side_a, (int, float)) and isinstance(side_b, (int, float))
            and isinstance(side_c, (int, float))):
        return "invalid"

    if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_d <= 0:
        return "invalid"

    if side_a == side_b and side_b == side_c and side_c == side_d:
        return "square"

    elif side_a == side_c and side_b == side_d:
        return "rectangle"

    else:
        return "invalid"


def get_quadrilateral_corners_type(side_a=0, side_b=0, side_c=0, side_d=0,
                                   corner_ab=0, corner_bc=0, corner_cd=0, corner_ad=0):
    """
    Determine if the given Quadrilateral is side_a rectangle, square, or rhombus

    :param side_a: line side_a
    :type side_a: float or int or tuple or list or dict

    :param side_b: line side_b
    :type side_b: float

    :param side_c: line side_c
    :type c: float

    :param side_d: line side_d
    :type side_d: float

    :param corner_ab: corner corner_ab
    :type corner_ab: float

    :param corner_bc: corner corner_bc
    :type corner_bc: float

    :param corner_cd: corner corner_cd
    :type corner_cd: float

    :param corner_ad: corner corner_ad
    :type corner_ad: float

    :return: "rectangle", "square", "rhombus", "invalid", or "disconnected"
    :rtype: str
    """
    if isinstance(side_a, (tuple, list)) and len(side_a) == 8:
        corner_ad = side_a[7]
        corner_cd = side_a[6]
        corner_bc = side_a[5]
        corner_ab = side_a[4]
        side_d = side_a[3]
        side_c = side_a[2]
        side_b = side_a[1]
        side_a = side_a[0]

    if isinstance(side_a, dict) and len(side_a.keys()) == 8:
        values = []
        for value in side_a.values():
            values.append(value)
        side_a = values[0]
        side_b = values[1]
        side_c = values[2]
        side_d = values[3]
        corner_ab = values[4]
        corner_bc = values[5]
        corner_cd = values[6]
        corner_ad = values[7]

    if not (isinstance(side_a, (int, float)) and isinstance(side_b, (int, float))
            and isinstance(side_c, (int, float))):
        return "invalid"

    if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_d <= 0 or \
                    corner_ab <= 0 or corner_bc <= 0 or corner_cd <= 0 or corner_ad <= 0:
        return "invalid"

    if side_a == side_b and side_b == side_c and side_c == side_d and \
                    corner_ab == 90 and corner_ab == corner_bc and \
                    corner_bc == corner_cd and corner_cd == corner_ad:
        return "square"

    elif side_a == side_c and side_b == side_d and corner_ab == 90 and \
                    corner_ab == corner_bc and corner_bc == corner_cd and corner_cd == corner_ad:
        return "rectangle"

    elif side_a == side_b and side_b == side_c and side_c == side_d and \
                    corner_ad == corner_bc and corner_ab == corner_cd and\
                    (corner_ad + corner_ab) == 180:
        return "rhombus"

    else:
        return "disconnected"
