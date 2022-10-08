from easyAI import TwoPlayerGame, Human_Player, AI_Player

class Battleships ():
    def __init__(self, players):
        self.players = players
        self.board_1 = [[0 for x in range(6)] for y in range(6)]
        self.board_2 = [[0 for x in range(6)] for y in range(6)]
    
    def getBoard(self):
        print(self.board_1)
        print(self.board_2)


def main():
    battleships = Battleships(["1", "2"])
    battleships.getBoard()

main()


