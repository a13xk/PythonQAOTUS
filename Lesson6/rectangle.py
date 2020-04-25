from Lesson6.geometric_figure import GeometricFigure


class Rectangle(GeometricFigure):

    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, angles=4)

        # Define rectangle by 2 sides
        if kwargs.get("side_a") and kwargs.get("side_b"):
            self.side_a = kwargs.get("side_a")  # Length of side A
            self.side_b = kwargs.get("side_b")  # Length of side B

            if type(self.side_a) != float:
                raise ValueError(f"Invalid type of rectangle side A: {type(self.side_a)}")
            if type(self.side_b) != float:
                raise ValueError(f"Invalid type of rectangle side B: {type(self.side_b)}")

            if self.side_a <= 0.0:
                raise ValueError(f"Invalid value of rectangle side A: {self.side_a}")
            if self.side_b <= 0.0:
                raise ValueError(f"Invalid value of rectangle side B: {self.side_b}")
    #

    @property
    def area(self) -> float:
        return self.side_a * self.side_b
    #

    @property
    def perimeter(self) -> float:
        return (self.side_a + self.side_b) * 2
    #

    def add_area(self, figure):
        super().add_area(figure=figure)
    #
#
