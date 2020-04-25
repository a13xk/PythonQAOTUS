from Lesson6.geometric_figure import GeometricFigure


class Square(GeometricFigure):

    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, angles=4)

        # Define square by 1 side
        if kwargs.get("side_a"):
            self.side_a = kwargs.get("side_a")  # Length of side A

            if type(self.side_a) != float:
                raise ValueError(f"Invalid type of square side A: {type(self.side_a)}")
            if self.side_a <= 0.0:
                raise ValueError(f"Invalid value of square side A: {self.side_a}")
    #

    def area(self) -> float:
        return self.side_a * self.side_a
    #

    def perimeter(self) -> float:
        return (self.side_a + self.side_a) * 2
    #

    def add_area(self, figure):
        super().add_area(figure=figure)
    #
#
