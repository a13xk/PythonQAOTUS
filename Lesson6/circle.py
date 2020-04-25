from Lesson6.geometric_figure import GeometricFigure
import math


class Circle(GeometricFigure):

    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, angles=0)

        # Define circle by radius
        if kwargs.get("radius"):
            self.radius = kwargs.get("radius")  # Length of circle radius

            if type(self.radius) != float:
                raise ValueError(f"Invalid type of circle radius: {type(self.radius)}")
            if self.radius <= 0.0:
                raise ValueError(f"Invalid value of circle radius: {self.radius}")
    #

    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)
    #

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    #

    def add_area(self, figure):
        super().add_area(figure=figure)
    #
#
