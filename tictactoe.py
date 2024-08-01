board = ['     ' for _ in range(9)]  # 3x3 board

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1  # AI wins
    if check_winner(board, 'X'):
        return -1 # Human wins
    if is_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print('-'*5)

def play_game():
    board = [' ' for _ in range(9)]
    print_board(board)
    
    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'X'
        else:
            print("Invalid move, try again.")
            continue
        
        if check_winner(board, 'X'):
            print_board(board)
            print("Human wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        move = best_move(board)
        board[move] = 'O'
        
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        print_board(board)

play_game()
