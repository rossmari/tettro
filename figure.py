class Figure:

    points = None
    coordinates = {'row': 0, 'col': 5}

    width = 0
    height = 0

    def value_at(self, row, col):
        return self.points[row][col]

    # describe figure
    def __init__(self):

        self.height = self.points.len()
        self.width = self.points[0].len()

    # move figure down to one row - as gravity do it
    def fall(self):
        self.coordinates['row'] += 1

    # todo : move figure by user raised events, by 1 col per function call
    def move_right(self):
        self.move(True)

    def move_left(self):
        self.move(False)

    def move(self, side):
        if side:
            self.coordinates['col'] += 1
        else:
            self.coordinates['col'] -= 1


class Pillar(Figure):

    points = [
        [1],
        [1],
        [1],
        [1],
    ]

    coordinates = {'row': 0, 'col': 5}


class JFigure(Figure):

    points = [
        [1], [1], [1],
        [0], [0], [1],
    ]

    coordinates = {'row': 0, 'col': 3}


class LFigure(Figure):

    points = [
        [1], [1], [1],
        [1], [0], [0],
    ]

    coordinates = {'row': 0, 'col': 3}