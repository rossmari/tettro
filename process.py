from field import Field


class GameProcess:

    field = None

    def __init__(self):
        self.field = Field()

    def start_game(self):
        # start game process
        for step in range(0, 50):
            self.field.process_gravity()

            for row in range(0, 22):
                print self.field.moveFrame[row]

            print "next move"


# =======================
process = GameProcess()
process.start_game()




