from config import *
from utils import get_all_moves

class Agents:
    def __init__(self):
        self.total_nodes = 0
        self.pruned_nodes = 0

    def minimax(self, position, depth, max_player, game):
        if depth == 0 or position.winner() is not None:
            return position.evaluate(), position

        if max_player:
            max_eval = float('-inf')
            best_move = None
            for move in get_all_moves(position, BLACK, game):
                evaluation, _ = self.minimax(move, depth - 1, False, game)
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in get_all_moves(position, RED, game):
                evaluation, _ = self.minimax(move, depth - 1, True, game)
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
            return min_eval, best_move

    def alpha_beta(self, position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
        self.total_nodes += 1  # Increment nodes count

        if depth == 0 or position.winner() is not None:
            return position.evaluate(), position

        best_move = None

        if max_player:
            max_eval = float('-inf')
            for move in get_all_moves(position, BLACK, game, show_moves=False):
                evaluation, _ = self.alpha_beta(move, depth - 1, False, game, alpha, beta)
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    self.pruned_nodes += 1
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in get_all_moves(position, RED, game, show_moves=False):
                evaluation, _ = self.alpha_beta(move, depth - 1, True, game, alpha, beta)
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, min_eval)
                if beta <= alpha:
                    self.pruned_nodes += 1
                    break
            return min_eval, best_move
        
    def print_stats(self):
        if self.total_nodes > 0:
            percentage_pruned = (self.pruned_nodes / self.total_nodes) * 100
            print(f"Total Nodes: {self.total_nodes}, Pruned Nodes: {self.pruned_nodes}, Percentage Pruned: {percentage_pruned:.2f}%")
        else:
            print("No nodes were processed.")
