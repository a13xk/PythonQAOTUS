from Lesson6.geometric_figure import GeometricFigure
import math


class Triangle(GeometricFigure):
    """
    Triangle
    """
    triangle_is_equilateral: bool = False
    triangle_is_right: bool = False

    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, angles=3)

        # Define triangle by 3 sides
        if kwargs.get("side_a") and kwargs.get("side_b") and kwargs.get("side_c"):
            self.side_a = kwargs.get("side_a")  # Length of side A
            self.side_b = kwargs.get("side_b")  # Length of side B
            self.side_c = kwargs.get("side_c")  # Length of side C

            if type(self.side_a) != float:
                raise ValueError(f"Invalid type of triangle side A: {type(self.side_a)}")
            if type(self.side_b) != float:
                raise ValueError(f"Invalid type of triangle side B: {type(self.side_b)}")
            if type(self.side_c) != float:
                raise ValueError(f"Invalid type of triangle side C: {type(self.side_c)}")
            if self.side_a + self.side_b < self.side_c or self.side_a + self.side_c < self.side_b or self.side_b + self.side_c < self.side_a:
                raise ValueError("Triangle cannot be defined by specified sides")

            # Equilateral triangle
            if math.isclose(self.side_a, self.side_b) and math.isclose(self.side_b, self.side_c):
                self.triangle_is_equilateral = True

            # Right triangle
            if math.isclose(self.side_a ** 2, self.side_b ** 2 + self.side_c ** 2):
                self.triangle_is_right = True
                self.leg_a = self.side_b
                self.leg_b = self.side_c
            if math.isclose(self.side_b ** 2, self.side_a ** 2 + self.side_c ** 2):
                self.triangle_is_right = True
                self.leg_a = self.side_a
                self.leg_b = self.side_c
            if math.isclose(self.side_c ** 2, self.side_a ** 2 + self.side_b ** 2):
                self.triangle_is_right = True
                self.leg_a = self.side_a
                self.leg_b = self.side_b

    #

    @property
    def area(self) -> float:
        if self.triangle_is_equilateral:
            return self.side_a ** 2 * math.sqrt(3.0) / 4.0
        elif self.triangle_is_right:
            return self.leg_a * self.leg_b / 2.0
        else:
            p = self.perimeter / 2.0
            return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
    #

    @property
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
    #

    def add_area(self, figure):
        super().add_area(figure=figure)
    #
#
