import math

import pytest

from Lesson6.circle import Circle
from Lesson6.rectangle import Rectangle
from Lesson6.square import Square
from Lesson6.triangle import Triangle


class TestRectangle:

    @pytest.mark.parametrize(
        argnames="name,expected_name",
        argvalues=[
            ("The circle", "The circle"),
            (123, "123"),
            (None, "None")
        ]
    )
    def test_name(self, name, expected_name):
        rectangle = Rectangle(name=name, side_a=1.23, side_b=3.21)
        assert rectangle.name == expected_name
    #

    def test_angles(self):
        rectangle = Rectangle(name="The rectangle", side_a=1.23, side_b=3.21)
        assert rectangle.angles == 4
    #

    @pytest.mark.parametrize(
        argnames="side_a,side_b,expected_area",
        argvalues=[
            (1.0, 1.0, 1.000),
            (1.23, 3.21, 3.948),
            (123.456, 654.321, 80779.853)
        ]
    )
    def test_area(self, side_a, side_b, expected_area):
        rectangle = Rectangle(name="The rectangle", side_a=side_a, side_b=side_b)
        calculated_area = rectangle.area
        assert math.isclose(calculated_area, expected_area, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="side_a,side_b,expected_perimeter",
        argvalues=[
            (1.0, 1.0, 4.000),
            (1.23, 3.21, 8.879),
            (123.456, 654.321, 1555.554)
        ]
    )
    def test_perimeter(self, side_a, side_b, expected_perimeter):
        rectangle = Rectangle(name="The rectangle", side_a=side_a, side_b=side_b)
        calculated_perimeter = rectangle.perimeter
        assert math.isclose(calculated_perimeter, expected_perimeter, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="other_figure, expected_areas_sum",
        argvalues=[
            (Circle(name="Valid circle", radius=1.23), 8.701),
            (Square(name="Valid square", side_a=4.56), 24.741),
            (Triangle(name="Valid triangle", side_a=1.23, side_b=2.34, side_c=3.45), 4.697)
        ],
        ids=[
            "Rectangle",
            "Square",
            "Triangle"
        ]
    )
    def test_add_area(self, other_figure, expected_areas_sum):
        rectangle = Rectangle(name="The rectangle", side_a=1.23, side_b=3.21)
        area_sum = rectangle.add_area(other_figure)
        assert math.isclose(area_sum, expected_areas_sum, rel_tol=0.01), \
            f"Expected sum of areas: {expected_areas_sum}\nActual sum of areas: {area_sum}"
    #
#
