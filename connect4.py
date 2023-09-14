import numpy as np
import pygame
import sys
import math
from tkinter import *

# Constants for colors and board dimensions
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ROW_COUNT = 6
COLUMN_COUNT = 7

# Define the Connect 4 game within a function
def connect_four_game():
    # Functions for the game logic
    def create_board():
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 0))

    def winning_move(board, piece):
        # Check horizontal locations for winning
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        # Check vertical locations for winning
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # Check positively diagonals for winning
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        # Check negatively diagonals for winning
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    # Initialize the game
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # Ask Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render(p1_entry.get() + " wins!", 1, RED)
                            screen.blit(label, (100, 10))
                            game_over = True

                # Ask Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render(p2_entry.get()+" wins!", 1, YELLOW)
                            screen.blit(label, (100, 10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)

# Function to check if both player names are entered
def are_player_names_entered():
    return p1_entry.get() and p2_entry.get()

# tkinter
root = Tk()
root.title("Connect 4 by Mina Robir")
root.geometry('600x600')
# Top frame for labels and player name entry
top_frame = Frame()
label_text = Label(top_frame, text="Connect 4 Game by Mina Robir", font=('consolas', 28))
label_text.pack(side="top")
text_content = Label(top_frame, text="Please enter your names", font=('consolas', 26))
text_content.pack(side="top")

# Player 1 Entry
p1_text = Label(top_frame, text="Player 1", font=('Arial', 20))
p1_text.pack(pady=20)
p1_entry = Entry(top_frame, font=('Arial', 20), width=10)
p1_entry.pack(pady=10)

# Player 2 Entry
p2_text = Label(top_frame, text="Player 2", font=('Arial', 20))
p2_text.pack(pady=20)
p2_entry = Entry(top_frame, font=('Arial', 20), width=10)
p2_entry.pack(pady=10)

# Display Top frame
top_frame.pack()

# Bottom frame for the "Start the game" button
bottom_frame = Frame()
start_game_button = Button(bottom_frame, text="Start the game", relief = "raised", bg='cyan', font=("Heelvetica", 24), command=connect_four_game)


# Bind a function to check for player names when a key is released in the text fields
def check_player_names(event):
    if are_player_names_entered():
        start_game_button.pack(side="bottom", pady=30)
    else:
        start_game_button.pack_forget()
        
p1_entry.bind("<KeyRelease>", check_player_names)
p2_entry.bind("<KeyRelease>", check_player_names)

# Display bottom frame
bottom_frame.pack()

root.mainloop()
