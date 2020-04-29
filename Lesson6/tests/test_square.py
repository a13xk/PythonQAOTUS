import math

import pytest

from Lesson6.circle import Circle
from Lesson6.rectangle import Rectangle
from Lesson6.square import Square
from Lesson6.triangle import Triangle


class TestSquare:

    @pytest.mark.parametrize(
        argnames="name,expected_name",
        argvalues=[
            ("The square", "The square"),
            (123, "123"),
            (None, "None")
        ]
    )
    def test_name(self, name, expected_name):
        square = Square(name=name, side_a=1.23)
        assert square.name == expected_name
    #

    def test_angles(self):
        square = Square(name="The square", side_a=1.23)
        assert square.angles == 4
    #

    @pytest.mark.parametrize(
        argnames="side_a,expected_area",
        argvalues=[
            (1.0, 1.000),
            (1.23, 1.5129),
            (123.456, 15241.383)
        ]
    )
    def test_area(self, side_a, expected_area):
        square = Square(name="The square", side_a=side_a)
        calculated_area = square.area
        assert math.isclose(calculated_area, expected_area, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="side_a,expected_perimeter",
        argvalues=[
            (1.0, 4.000),
            (1.23, 4.920),
            (123.456, 493.824)
        ]
    )
    def test_perimeter(self, side_a, expected_perimeter):
        square = Square(name="The square", side_a=side_a)
        calculated_perimeter = square.perimeter
        assert math.isclose(calculated_perimeter, expected_perimeter, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="other_figure, expected_areas_sum",
        argvalues=[
            (Circle(name="Valid circle", radius=1.23), 6.265),
            (Rectangle(name="Valid rectangle", side_a=1.23, side_b=4.56), 7.121),
            (Triangle(name="Valid triangle", side_a=1.23, side_b=2.34, side_c=3.45), 2.262)
        ],
        ids=[
            "Circle",
            "Rectangle",
            "Triangle"
        ]
    )
    def test_add_area(self, other_figure, expected_areas_sum):
        square = Square(name="The square", side_a=1.23)
        area_sum = square.add_area(other_figure)
        assert math.isclose(area_sum, expected_areas_sum, rel_tol=0.01), \
            f"Expected sum of areas: {expected_areas_sum}\nActual sum of areas: {area_sum}"
    #
#
