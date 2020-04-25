import math

import pytest

from Lesson6.circle import Circle
from Lesson6.rectangle import Rectangle
from Lesson6.square import Square
from Lesson6.triangle import Triangle


class TestCircle:

    @pytest.mark.parametrize(
        argnames="name,expected_name",
        argvalues=[
            ("The circle", "The circle"),
            (123, "123"),
            (None, "None")
        ]
    )
    def test_name(self, name, expected_name):
        circle = Circle(name=name, radius=1.23)
        assert circle.name == expected_name
    #

    def test_angles(self):
        circle = Circle(name="The circle", radius=1.23)
        assert circle.angles == 0
    #

    @pytest.mark.parametrize(
        argnames="radius,expected_area",
        argvalues=[
            (1.0, 3.141),
            (1.23, 4.752),
            (123.456, 47882.219)
        ]
    )
    def test_area(self, radius, expected_area):
        circle = Circle(name="The circle", radius=radius)
        calculated_area = circle.area
        assert math.isclose(calculated_area, expected_area, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="radius,expected_perimeter",
        argvalues=[
            (1.0, 6.283),
            (1.23, 7.728),
            (123.456, 775.696)
        ]
    )
    def test_perimeter(self, radius, expected_perimeter):
        circle = Circle(name="The circle", radius=radius)
        calculated_perimeter = circle.perimeter
        assert math.isclose(calculated_perimeter, expected_perimeter, rel_tol=0.001)
    #

    @pytest.mark.parametrize(
        argnames="other_figure, expected_areas_sum",
        argvalues=[
            (Rectangle(name="Valid rectangle", side_a=1.23, side_b=3.21), 32.22),
            (Square(name="Valid square", side_a=4.56), 49.06),
            (Triangle(name="Valid triangle", side_a=1.23, side_b=2.34, side_c=3.45), 29.02)
        ],
        ids=[
            "Rectangle",
            "Square",
            "Triangle"
        ]
    )
    def test_add_area(self, other_figure, expected_areas_sum):
        circle = Circle(name="The circle", radius=3.0)
        area_sum = circle.add_area(other_figure)
        assert math.isclose(area_sum, expected_areas_sum, rel_tol=0.01), \
            f"Expected sum of areas: {expected_areas_sum}\nActual sum of areas: {area_sum}"
    #
#
