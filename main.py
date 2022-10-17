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
        print ("   ====   ")
        for row in self.board_2:
            print(row)

    def add_ship(self, ship_class, player, position):
        if ship_class > 1:
            pass
        else:
            self.board_1[position[0]][position[1]] = 1 

    
    def add_big_ship(self, ship_class, player, position_start, position_end):
        if abs(position_end[0] - position_start[0]) != ship_class - 1 and abs(position_end[1] - position_start[1]) != ship_class - 1:
            return

        self.board_1[position_start[0]][position_start[1]] = 1
        self.board_1[position_end[0]][position_end[1]] = 1
        
        print(position_start[1], position_end[1])
        
        if position_start[0] != position_end[0]:
            if position_start[0] > position_end[0]:
                self.board_1[position_start[0] - 1][position_start[1]] = 1
            else:
                self.board_1[position_start[0] + 1][position_start[1]] = 1
        else:
            if position_start[1] > position_end[1]:
                self.board_1[position_start[0]][position_start[1] - 1] = 1
            else:
                self.board_1[position_start[0]][position_end[1] + 1] = 1
        

    def shoot(self, position, player):
        if self.board_1[position[0]][position[1]] == 1:
            self.board_1[position[0]][position[1]] = 2


##############
# ship codes:
# 1 = there is a ship there
# 2 = ship hit
# 3 = TODO = ship sunken


def main():
    battleships = Battleships(["1", "2"])
    battleships.add_ship(1, 1, (1,3))
    battleships.add_big_ship(3, 1, (4,5), (4,3))
    battleships.add_big_ship(2, 1, (2,2), (3,2))
    battleships.shoot((2,2), 2)
    battleships.get_board()

main()


