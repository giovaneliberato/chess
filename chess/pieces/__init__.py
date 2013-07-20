class ImpossibleMove(Exception):
    pass


class CantInstantiatePiece(Exception):
    pass


class InvalidChessColor(Exception):
    pass


class Piece(object):
    def __init__(self, color):

        if self.__class__.__name__ == 'Piece':
            raise CantInstantiatePiece("You can't instantiate this class")

        color = color.lower()
        if color not in ['white', 'black']:
            raise InvalidChessColor('That color should be "black" or "white".')

        self.__color = color
        self.y = '12345678'
        self.x = 'abcdefgh'

    def __str__(self):
        return self.__class__.__name__

    def is_black(self):
        return self.__color == 'black'

    def is_white(self):
        return self.__color == 'white'


class Bishop(Piece):
    def move(self, _from, to):
        if abs(self.x.index(_from[0]) - self.x.index(to[0])) == abs(self.y.index(to[1]) - self.y.index(_from[1])):
            return to
        raise ImpossibleMove("Bishop can't move to %s" % to)


class Rook(Piece):
    def move(self, _from, to):
        is_horizontal_and_valid = self.x.index(_from[0]) == self.x.index(to[0]) and self.y.index(_from[1]) != self.y.index(to[1])
        is_vertical_and_valid = self.x.index(_from[0]) != self.x.index(to[0]) and self.y.index(_from[1]) == self.y.index(to[1])

        if is_horizontal_and_valid or is_vertical_and_valid:
            return to
        raise ImpossibleMove("Rook can't move to %s" % to)


class King(Piece):
    def move(self, _from, to):
        x_distance = abs(self.x.index(_from[0]) - self.x.index(to[0]))
        y_distance = abs(self.y.index(_from[1]) - self.y.index(to[1]))

        if x_distance in [0, 1] and y_distance in [0, 1] and x_distance + y_distance != 0:
            return to
        raise ImpossibleMove("King can't move to %s" % to)


class Queen(Piece):
    def move(self, _from, to):

        # move as a Rook {{
        is_horizontal_and_valid = self.x.index(_from[0]) == self.x.index(to[0]) and self.y.index(_from[1]) != self.y.index(to[1])
        is_vertical_and_valid = self.x.index(_from[0]) != self.x.index(to[0]) and self.y.index(_from[1]) == self.y.index(to[1])

        if is_horizontal_and_valid or is_vertical_and_valid:
            return to
        # }}

        # move as a Bishop {{
        if abs(self.x.index(_from[0]) - self.x.index(to[0])) == abs(self.y.index(to[1]) - self.y.index(_from[1])):
            return to
        # }}

        raise ImpossibleMove("Queen can't move to %s" % to)


class Pawn(Piece):
    def move(self, _from, to):
        if self.x.index(_from[0]) == self.x.index(to[0]) and abs(self.y.index(to[1]) - self.y.index(_from[1])) == 1:
            return to
        raise ImpossibleMove("Pawn can't move to %s" % to)


class Knight(Piece):
    def move(self, _from, to):
        x_distance = abs(self.x.index(_from[0]) - self.x.index(to[0]))
        y_distance = abs(self.y.index(_from[1]) - self.y.index(to[1]))

        if x_distance in [1, 2] and y_distance in [1, 2] and x_distance != y_distance:
            return to
        raise ImpossibleMove("Knight can't move to %s" % to)