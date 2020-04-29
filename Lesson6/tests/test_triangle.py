import math

import pytest

from Lesson6.circle import Circle
from Lesson6.rectangle import Rectangle
from Lesson6.square import Square
from Lesson6.triangle import Triangle


class TestTriangle:

    @pytest.mark.parametrize(
        argnames="name,expected_name",
        argvalues=[
            ("The triangle", "The triangle"),
            (123, "123"),
            (None, "None")
        ]
    )
    def test_name(self, name, expected_name):
        triangle = Triangle(name=name, side_a=1.23, side_b=2.34, side_c=3.45)
        assert triangle.name == expected_name
    #

    def test_angles(self):
        triangle = Triangle(name="The triangle", side_a=1.23, side_b=2.34, side_c=3.45)
        assert triangle.angles == 3
    #

    @pytest.mark.parametrize(
        argnames="side_a,side_b,side_c,expected_area",
        argvalues=[
            (1.0, 1.0, 1.0, 0.433),
            (1.23, 2.34, 3.45, 0.749),
            (123.456, 123.456, 234.567, 4521.069)
        ]
    )
    def test_area(self, side_a, side_b, side_c, expected_area):
        triangle = Triangle(name="The triangle", side_a=side_a, side_b=side_b, side_c=side_c)
        calculated_area = triangle.area
        assert math.isclose(calculated_area, expected_area, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="side_a,side_b,side_c,expected_perimeter",
        argvalues=[
            (1.0, 1.0, 1.0, 3.0),
            (1.23, 2.34, 3.45, 7.020),
            (123.456, 123.456, 234.567, 481.479)
        ]
    )
    def test_perimeter(self, side_a, side_b, side_c, expected_perimeter):
        triangle = Triangle(name="The triangle", side_a=side_a, side_b=side_b, side_c=side_c)
        calculated_perimeter = triangle.perimeter
        assert math.isclose(calculated_perimeter, expected_perimeter, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="other_figure, expected_areas_sum",
        argvalues=[
            (Circle(name="Valid circle", radius=1.23), 5.502),
            (Square(name="Valid square", side_a=4.56), 21.543),
            (Rectangle(name="Valid rectangle", side_a=1.23, side_b=3.21), 4.697)
        ],
        ids=[
            "Circle",
            "Square",
            "Rectangle"
        ]
    )
    def test_add_area(self, other_figure, expected_areas_sum):
        triangle = Triangle(name="The triangle", side_a=1.23, side_b=2.34, side_c=3.45)
        area_sum = triangle.add_area(other_figure)
        assert math.isclose(area_sum, expected_areas_sum, rel_tol=0.01), \
            f"Expected sum of areas: {expected_areas_sum}\nActual sum of areas: {area_sum}"
    #
#
