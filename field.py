from figure_generator import FigureGenerator
from copy import copy


class Field:
    # contains some kind of matrix for field points
    rows = 22
    columns = 10

    fieldPoints = None
    name = ''
    activeFigure = None
    figureGenerator = None

    def __init__(self, name):
        self.name = name
        self.clear_field()
        self.figureGenerator = FigureGenerator()

    def clear_field(self):
        self.fieldPoints = [[0] * self.columns] * self.rows

    def process_gravity(self):
        if not self.activeFigure:
            self.activeFigure = self.generate_figure()

        if self.can_move_figure():
            self.activeFigure.fall()
        else:
            self.activeFigure = None
            self.fieldPoints = self.render_field()

        # try to destroy some full rows if they exist
        self.destroy_full_rows()

        # process activeFigureMove

    def can_move_figure(self):
        # todo : check position relative to field borders
        # todo : check figure structure relative to other field points
        return True

    # full rows destroying
    def destroy_full_rows(self):
        row = self.find_full_row()
        if row:
            self.destroy_full_row(row)
            self.destroy_full_rows()

    def find_full_row(self):
        for row in self.rows:
            if all(self.fieldPoints[row]):
                return row

        return None

    def destroy_full_row(self, row_index):
        # you should move down all rows that => than 'row_index'
        # to -1 position
        for row in range(row_index, 0, -1):
            if row - 1 < 0:
                row = [0] * self.columns

            self.fieldPoints[row] = self.fieldPoints[row - 1]

    def generate_figure(self):
        return self.figureGenerator.generate_figure()

    # field presentation
    def render_field(self):
        start = self.activeFigure.coordinates

        frame = copy.copy(self.fieldPoints)

        for row in self.activeFigure.height:
            for col in self.activeFigure.width:
                self.frame[start['y'] + row][start['x'] + col] = \
                    self.activeFigure[row][col]

        return frame
