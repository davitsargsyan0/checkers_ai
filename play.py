import pygame
from config import *
from utils import get_row_col_from_mouse
from algorithms import Agents
from game import Game

def play(red_player="user", black_player="maraion", red_maraion_depth=6, black_maraion_depth=6):
    """
    Play a game of checkers with configurable players and separate Maraion depths.
    
    Parameters:
    - red_player: "user" or "maraion" to specify the RED player type.
    - black_player: "user" or "maraion" to specify the BLACK player type.
    - red_maraion_depth: Depth for the RED Maraion's alpha-beta search.
    - black_maraion_depth: Depth for the BLACK Maraion's alpha-beta search.
    """
    global total_nodes, pruned_nodes 

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            winner = game.winner()
            print(f"Winner: {'BLACK' if winner == BLACK else 'RED'}")

            # Display the final score
            red_score = game.board.red_left + (game.board.red_kings * 0.5)
            black_score = game.board.black_left + (game.board.black_kings * 0.5)
            print(f"Final Score -> BLACK: {black_score}, RED: {red_score}")
            
            run = False
            continue

        if game.turn == BLACK:
            if black_player == "maraion":
                
                
                ai_engine = Agents()
                value, new_board = ai_engine.alpha_beta(game.get_board(), black_maraion_depth, True, game)
                
                total_nodes = ai_engine.total_nodes
                pruned_nodes = ai_engine.pruned_nodes
                
                if total_nodes > 0: 
                    percentage_pruned = pruned_nodes * 100 / total_nodes
                    print(f"BLACK Maraion -> Total Nodes: {total_nodes}, Pruned Nodes: {pruned_nodes}, Percentage Pruned: {percentage_pruned:.2f}%")
                
                game.ai_move(new_board)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)

        elif game.turn == RED:
            if red_player == "maraion":
                total_nodes = 0
                pruned_nodes = 0
                
                ai_engine = Agents()
                value, new_board = ai_engine.alpha_beta(game.get_board(), red_maraion_depth, False, game)
                
                if total_nodes > 0: 
                    percentage_pruned = pruned_nodes * 100 / total_nodes
                    print(f"RED Maraion -> Total Nodes: {total_nodes}, Pruned Nodes: {pruned_nodes}, Percentage Pruned: {percentage_pruned:.2f}%")
                
                game.ai_move(new_board)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)

        game.update()
    
    pygame.quit()
