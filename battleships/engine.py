import random


class Ship:
    def __init__(self, size):
        """ Ship class
            Used to create a new ship object
            Defines the size and vertical or horizontal positioning
        """
        self.row = random.randrange(0, 9)
        self.col = random.randrange(0, 9)
        self.size = size
        self.orientation = random.choice(["h", "v"])
        self.indexes = self.compute_indexes()

    def compute_indexes(self):
        """Compute_indexes

        Returns:
            Indexes of all the ships created
        """
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i * 10 for i in range(self.size)]


class Player:
    def __init__(self):
        """Player class
            Used to create a new player object
            with it's ships.
        """
        self.ships = []
        self.search = ["U" for i in range(100)]  # "U" is for "unknown"
        self.place_ships(sizes=[5, 4, 3, 3, 2])
        list_of_lists = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in list_of_lists for index in sublist]

    def place_ships(self, sizes):

        for size in sizes:
            placed = False
            while not placed:

                """ Create a new ship instance"""
                ship = Ship(size)

                """ Check if placement is possible based on used indexes """
                possible = True
                for i in ship.indexes:

                    """ Indexes must be < 100: as the board is 10x10"""
                    if i >= 100:
                        possible = False
                        break

                    """ Ships cannot occupy same rows """
                    new_row = i // 10
                    new_col = i % 10
                    if new_row != ship.row and new_col != ship.col:
                        possible = False
                        break

                    """ Ships cannot intersect: """
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible = False
                            break

                """ Ship placement """
                if possible:
                    self.ships.append(ship)
                    placed = True

    def show_ships(self):
        """Show created ships"""
        indexes = ["-" if i not in self.indexes else "X" for i in range(100)]
        for row in range(10):
            print(" ".join(indexes[(row - 1) * 10:row * 10]))


class Game:
    """Definition of a new Game instance
    """
    def __init__(self, human1, human2):
        self.human1 = human1
        self.human2 = human2
        self.player1 = Player()
        self.player2 = Player()
        self.player1_turn = True
        self.computer_turn = True if not self.human1 else False
        self.over = False
        self.result = None

    def make_move(self, i):
        """ Move continuation after hitting the ship """
        player = self.player1 if self.player1_turn else self.player2
        opponent = self.player2 if self.player1_turn else self.player1
        hit = False

        if i in opponent.indexes:
            """ Set miss dot color "M" or hit color "H" """
            player.search[i] = "H"
            hit = True

            """ Check if ship is sunk and set color "S" """
            for ship in opponent.ships:
                sunk = True
                for i in ship.indexes:
                    if player.search[i] == "U":
                        sunk = False
                        break
                if sunk:
                    for i in ship.indexes:
                        player.search[i] = "S"
        else:
            player.search[i] = "M"

        game_over = True
        """ Game over check """
        for i in opponent.indexes:
            if player.search[i] == "U":
                game_over = False
        self.over = game_over
        self.result = 1 if self.player1_turn else 2

        """ Change turns """
        if not hit:
            self.player1_turn = not self.player1_turn

            """ Switch between human and computer turn """
            if (self.human1 and not self.human2) or (not self.human1 and self.human2):
                self.computer_turn = not self.computer_turn

    def random_ai(self):
        """ Random_AI
            random moves for the AI
        """
        search = self.player1.search if self.player1_turn else self.player2.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        if len(unknown) > 0:
            random_index = random.choice(unknown)
            self.make_move(random_index)

    def basic_ai(self):
        """ Method for AI using neighbours searching and checkboard pattern moves"""
        search = self.player1.search if self.player1_turn else self.player2.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        hits = [i for i, square in enumerate(search) if square == "H"]

        """ Searching for the following squares of the ship after a hit """
        unknown_with_neighbours_hits1 = []
        unknown_with_neighbours_hits2 = []
        for u in unknown:
            if u + 1 in hits or u - 1 in hits or u - 10 in hits or u + 10 in hits:
                unknown_with_neighbours_hits1.append(u)
            if u + 2 in hits or u - 2 in hits or u - 20 in hits or u + 20 in hits:
                unknown_with_neighbours_hits2.append(u)

        """ Pick "U" square with direct and level-2 neighbour marked as "H" """
        for u in unknown:
            if u in unknown_with_neighbours_hits1 and u in unknown_with_neighbours_hits2:
                self.make_move(u)
                return

        """ Pick "U" square that has a neighbour marked as "H" """
        if len(unknown_with_neighbours_hits1) > 0:
            self.make_move(random.choice(unknown_with_neighbours_hits1))
            return

        """ Checker for the moves before a hit reduction"""
        checker_board = []
        for u in unknown:
            row = u // 10
            col = u % 10
            if (row + col) % 2 == 0:
                checker_board.append(u)
        if len(checker_board) > 0:
            self.make_move(random.choice(checker_board))
            return

        """ Random move """
        self.random_ai()
