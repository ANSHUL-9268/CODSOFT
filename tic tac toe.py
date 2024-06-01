import math

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    
    if ' ' not in board:
        return 'Tie'
    
    return None

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def best_move(board):
    best_val = -math.inf
    best_move = -1
    for move in get_available_moves(board):
        board[move] = 'O'
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move


def play_game():
    board = [' ' for _ in range(9)]
    human_turn = True

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"The winner is {winner}!")
            break

        if human_turn:
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'X'
                human_turn = False
            else:
                print("Invalid move, try again.")
        else:
            move = best_move(board)
            board[move] = 'O'
            human_turn = True

if __name__ == "__main__":
    play_game()
