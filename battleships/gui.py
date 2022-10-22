from engine import Game


import pygame
""" 
Game initialization 
pygame.init() : initialize imported pygame modules
pygame.font.init() : initialize font modules
pygame.display.set_caption("Battleship") : window name
myfont = pygame.font.SysFont("fresansttf", 100) :font
"""

pygame.init()
pygame.font.init()
pygame.display.set_caption("Battleship")
myfont = pygame.font.SysFont("fresansttf", 100)

""" Global variables
    needed for creating the grid and the window,
    as well as definig the AI player count.
"""
SQ_SIZE = 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
INDENT = 10
HUMAN1 = False
HUMAN2 = False

""" Colors """
GREY = (40, 50, 60)
WHITE = (255, 250, 250)
GREEN = (50, 200, 150)
RED = (250, 50, 100)
BLUE = (0, 80, 255)
ORANGE = (250, 140, 20)
COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED}



def draw_grid(player, left=0, top=0, search=False):
    """ Drawing a grid based on position
        on the screen and a one square pixel size
    """
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)
        if search:
            x += SQ_SIZE // 2
            y += SQ_SIZE // 2
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], (x, y), radius=SQ_SIZE // 4)


def draw_ships(player, left=0, top=0):
    """ Modeling and drawing the ships """
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT
        y = top + ship.row * SQ_SIZE + INDENT
        if ship.orientation == "h":
            width = ship.size * SQ_SIZE - 2 * INDENT
            height = SQ_SIZE - 2 * INDENT
        else:
            width = SQ_SIZE - 2 * INDENT
            height = ship.size * SQ_SIZE - 2 * INDENT
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=15)


game = Game(HUMAN1, HUMAN2)
""" New instance of a game
    
    animating = True
    pausing = False
    while animating: loop for all the possible moves while the game is ongoing   
"""
animating = True
pausing = False
while animating:

    """ Tracking user interaction """
    for event in pygame.event.get():

        """ Ending the game by closing the window """
        if event.type == pygame.QUIT:
            animating = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game.over:
            """ Getting the user mouse-click input by the coordinates
                x, y = pygame.mouse.get_pos()x, y = pygame.mouse.get_pos()
                if game.player1_turn : first player turn
                elif not game.player1_turn : second player turn
            """
            x, y = pygame.mouse.get_pos()
            if game.player1_turn and x < SQ_SIZE * 10 and y < 10 * SQ_SIZE:
                row = y // SQ_SIZE
                col = x // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)
            elif not game.player1_turn and x > WIDTH - SQ_SIZE * 10 and y > SQ_SIZE * 10 + V_MARGIN:
                row = (y - SQ_SIZE * 10 - V_MARGIN) // SQ_SIZE
                col = (x - SQ_SIZE * 10 - H_MARGIN) // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)

        """ Assigning a function to a certain types of action on a keyboard """
        if event.type == pygame.KEYDOWN:

            """" Escape key to close the animation """
            if event.key == pygame.K_ESCAPE:
                animating = False

            """ Space bar to pause and unpause the animation """
            if event.key == pygame.K_SPACE:
                pausing = not pausing

            """ Return key to restart the game """
            if event.key == pygame.K_RETURN:
                game = Game(HUMAN1, HUMAN2)

    """ Defining all of the GUI elements appearance """ 
    if not pausing:
        """ Draw background """ 
        SCREEN.fill(GREY)

        """ Draw search grids """ 
        draw_grid(game.player1, search=True)
        draw_grid(game.player2, search=True, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN,
                  top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)

        """ Draw position grids """
        draw_grid(game.player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_grid(game.player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)

        """ Draw ships onto position grids """ 
        draw_ships(game.player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_ships(game.player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)

        if not game.over and game.computer_turn:
            """ AI vs AI implementation 
                if game.player1_turn:
                    game.random_ai() : instance of an AI with random moves
                else:
                    game.basic_ai() : instance of an AI using checkboard pattern and searching for the neighbours
            """
            if game.player1_turn:
                game.random_ai()
            else:
                game.basic_ai()

        if game.over:
            """ Game over message appearing on the screen"""
            text = "Player " + str(game.result) + " wins!"
            textbox = myfont.render(text, False, GREY, WHITE)
            SCREEN.blit(textbox, (WIDTH // 2 - 240, HEIGHT // 2 - 50))

        pygame.time.wait(0)
        """Setting wait to a value > 0 will postpone the moves by the vaulue in ms"""
        pygame.display.flip()
        """ Updates all provided data on the screen """
