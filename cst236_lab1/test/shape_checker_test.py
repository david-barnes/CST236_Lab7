"""
Test for source.shape_checker
"""
from unittest import TestCase
from source.shape_checker import get_triangle_type, \
    get_quadrilateral_type, get_quadrilateral_corners_type

from test.plugins.ReqTracer import requirements


class TestGetTriangleType(TestCase):
    """ test cases for getting triangle type """

    @requirements(['#0001', '#0002'])
    def test_equilateral_all_int(self):
        """ test for equilateral triangle with int inputs """
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_equilateral_all_float(self):
        """ test for equilateral triangle with float inputs """
        result = get_triangle_type(1.5, 1.5, 1.5)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_scalene_all_int(self):
        """ test for scalene triangle """
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_isosceles_all_int(self):
        """ test for isosceles triangle """
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_triangle_invalid_int(self):
        """ test for invalid triangle """
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_triangle_invalid_char(self):
        """ test for invalid triangle with char inputs """
        result = get_triangle_type('a', 'b' 'c')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_triangle_tuple(self):
        """ test for equilateral triangle with int tuple input """
        tuple1 = (1, 1, 1)
        result = get_triangle_type(tuple1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_triangle_list(self):
        """ test for equilateral triangle with int list input """
        list1 = [1, 1, 1]
        result = get_triangle_type(list1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_triangle_dict(self):
        """ test for equilateral triangle with int dict input """
        dict1 = {'a':1, 'b': 1, 'c':1}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'equilateral')


class TestGetQuadrilateralType(TestCase):
    """ test cases for getting quadrilateral type """

    @requirements(['#0004'])
    def test_square_int(self):
        """ test for square with int inputs """
        result = get_quadrilateral_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    @requirements(['#0004'])
    def test_rectangle_int(self):
        """ test for rectangle with int inputs """
        result = get_quadrilateral_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0004'])
    def test_quad_invalid_char(self):
        """ test for invalid with char inputs """
        result = get_quadrilateral_type('1', '2', '1', '2')
        self.assertEqual(result, 'invalid')

    @requirements(['#0004'])
    def test_rectangle_float(self):
        """ test for rectangle with float inputs """
        result = get_quadrilateral_type(1.5, 2.5, 1.5, 2.5)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0004'])
    def test_square_tuple(self):
        """ test for square with int tuple input """
        tuple2 = (1, 1, 1, 1)
        result = get_quadrilateral_type(tuple2)
        self.assertEqual(result, 'square')

    @requirements(['#0004'])
    def test_rectangle_list(self):
        """ test for rectangle with int list input """
        list2 = [1, 2, 1, 2]
        result = get_quadrilateral_type(list2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0004'])
    def test_square_dict(self):
        """ test for square with int dict input """
        dict2 = {'a':1, 'b':1, 'c':1, 'd':1}
        result = get_quadrilateral_type(dict2)
        self.assertEqual(result, 'square')

    @requirements(['#0004'])
    def test_quad_invalid_zeros(self):
        """ test for invalid with zeros """
        result = get_quadrilateral_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0004'])
    def test_quad_invalid_int(self):
        """ test for invalid with int inputs """
        result = get_quadrilateral_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid')


class TestGetQuadrilateralWithCornersType(TestCase):
    """ test cases for getting quadrilateral type with corners """

    @requirements(['#0003', '#0004', '#0005'])
    def test_square_corners_int(self):
        """ test for square with int inputs """
        result = get_quadrilateral_corners_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_rectangle_corners_int(self):
        """ test for rectangle with int inputs """
        result = get_quadrilateral_corners_type(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_rhombus_corners_int(self):
        """ test for rhombus with int inputs """
        result = get_quadrilateral_corners_type(1, 1, 1, 1, 135, 45, 135, 45)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_invalid_corners_char(self):
        """ test for invalid with char inputs """
        result = get_quadrilateral_corners_type('1', '2', '1', '2', '90', '90', '90', '90')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_rectangle_corners_float(self):
        """ test for rectangle with float inputs """
        result = get_quadrilateral_corners_type(1.5, 2.5, 1.5, 2.5, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_square_corners_tuple(self):
        """ test for square with int tuple input """
        tuple3 = (1, 1, 1, 1, 90, 90, 90, 90)
        result = get_quadrilateral_corners_type(tuple3)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_rectangle_corners_list(self):
        """ test for rectangle with int list input """
        list3 = [1, 2, 1, 2, 90, 90, 90, 90]
        result = get_quadrilateral_corners_type(list3)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_square_corners_dict(self):
        """ test for square with int dict input """
        dict3 = {'a':1, 'b':1, 'c':1, 'd':1, 'ab':90, 'bc':90, 'cd':90, 'ad':90}
        result = get_quadrilateral_corners_type(dict3)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_invalid_corners_zeros(self):
        """ test for invalid with zeros """
        result = get_quadrilateral_corners_type(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_disconnected_corners_int(self):
        """ test for disconnected with int inputs """
        result = get_quadrilateral_corners_type(1, 2, 3, 4, 15, 25, 35, 45)
        self.assertEqual(result, 'disconnected')
