from field import Field


class GameProcess:

    field = None

    def __init__(self):
        self.field = Field()

    def start_game(self):
        # start game process
        while True:
            self.field.process_gravity()

            # todo : do some time out - for few seconds, before repeat loop







