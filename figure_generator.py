from figure import *
from random import *


# todo : how to rewrite this as singleton class of use module instead?
class FigureGenerator:

    def __init__(self):
        return None

    figures = [Pillar, JFigure, LFigure]

    def generate_figure(self):
        index = randint(0, len(self.figures) - 1)
        return self.figures[index]()
