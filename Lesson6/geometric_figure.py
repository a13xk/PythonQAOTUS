from __future__ import annotations  # To use GeometricFigure as type hint below


class GeometricFigure:

    def __init__(self, name: str, angles: int):
        self.name: str = str(name)
        self.angles: int = int(angles)
    #

    @property
    def area(self) -> float:
        """
        Area of geometric figure
        """
        return 0.0
    #

    @property
    def perimeter(self) -> float:
        """
        Perimeter of geometric figure
        """
        return 0.0
    #

    def add_area(self, figure: GeometricFigure):
        """
        Calculate area of 2 figures
        :param figure: Object of GeometricFigure class
        """
        if not issubclass(type(figure), GeometricFigure):
            raise NameError(f"Invalid type of object {figure}")
        return self.area + figure.area
    #
#

