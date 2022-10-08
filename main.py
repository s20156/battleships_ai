from easyAI import TwoPlayerGame, Human_Player, AI_Player

class Battleships ():
    def __init__(self, players):
        self.players = players
        self.board_1 = [[0 for x in range(6)] for y in range(6)]
        self.board_2 = [[0 for x in range(6)] for y in range(6)]
        self.hits_1 = []
        self.hits_2 = []
        self.ships_1 = []
        self.ships_2 = []
    
    def get_board(self):
        for row in self.board_1:
            print(row)
        print(self.board_2)

    def add_ship(self, ship_class, player, position):
        if ship_class > 1:
            pass
        else:
            self.board_1[position[0]][position[1]] = 1 


def main():
    battleships = Battleships(["1", "2"])
    battleships.add_ship(1, 1, (1,3))
    battleships.get_board()

main()


