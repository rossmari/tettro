from figure_generator import FigureGenerator
from copy import deepcopy


class Field:
    # contains some kind of matrix for field points
    rows = 22
    columns = 10

    fieldPoints = None
    activeFigure = None
    figureGenerator = None

    moveFrame = None

    def __init__(self):
        self.clear_field()
        self.figureGenerator = FigureGenerator()

    def clear_field(self):
        self.fieldPoints = [[0 for column in range(0, self.columns)] for row in range(self.rows)]

    def process_gravity(self):
        if not self.activeFigure:
            self.activeFigure = self.generate_figure()

        if self.can_move_figure():
            self.activeFigure.fall()
            self.moveFrame = self.render_field()
        else:
            self.fieldPoints = self.render_field()
            self.activeFigure = None

        # try to destroy some full rows if they exist
        self.destroy_full_rows()

    def can_move_figure(self):

        return self.can_move_down() and self.can_move_sides(+1) and \
            self.can_move_sides(-1)

    def can_move_sides(self, side):
        figure = self.activeFigure
        p = figure.coordinates

        for row in range(0, figure.height):
            for col in range(0, figure.width):
                if figure.value_at(row, col):
                    if self.fieldPoints[p['row'] + row][p['col'] + side]:
                        return False
        return True

    def can_move_down(self):
        figure = self.activeFigure
        figure_position = figure.coordinates

        return figure_position['row'] + figure.height < self.rows and \
            figure_position['col'] + figure.width < self.columns

    # full rows destroying
    def destroy_full_rows(self):
        row = self.find_full_row()
        if row:
            self.destroy_full_row(row)
            self.destroy_full_rows()

    def find_full_row(self):
        for row in range(0, self.rows):
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

        frame = deepcopy(self.fieldPoints)

        for row in range(0, self.activeFigure.height):
            for col in range(0, self.activeFigure.width):
                frame[start['row'] + row][start['col'] + col] = \
                    self.activeFigure.points[row][col]

        return frame
