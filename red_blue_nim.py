import sys

# evaluate function to calculate score
def eval_func(red, blue):
    red_score = red * 2
    blue_score = blue * 3
    return red_score + blue_score

# function to generate all possible moves
def best_possible_moves(red, blue):
    return [[red, blue-1] for blue in range(1, blue+1)] + \
           [[red-1, blue] for red in range(1, red+1)]

# implementation of min-max algorithm with alpha-beta pruning
def minmax_alphabetaprune(red, blue, depth, alpha=float('-inf'), beta=float('+inf'), is_maximizing=True):
    if red == 0 or blue == 0:
        if is_maximizing:
            return -1, None
        else:
            return 1, None

         # base case: if maximum depth is reached, return score
    if depth == 0:
        return eval_func(red, blue), None
    # if current player is maximizing, find the move that maximizes the score
    if is_maximizing:
        current_eval = float('-inf')
        best_move = None
        for move in best_possible_moves(red, blue):
            # recursively evaluate the move
            min_eval, D = minmax_alphabetaprune(move[0], move[1], depth - 1, alpha, beta, False)
            if min_eval > current_eval:
                current_eval = min_eval
                best_move = move
            if current_eval >= beta:
                return current_eval, move
            alpha = max(alpha, current_eval)
        return current_eval, best_move
    else:
        current_eval = float('+inf')
        best_move = None
        for move in best_possible_moves(red, blue):
            max_eval, D = minmax_alphabetaprune(move[0], move[1], depth - 1, alpha, beta, True)
            if max_eval < current_eval:
                current_eval = max_eval
                best_move = move
            if current_eval <= alpha:
                return current_eval, move
            beta = min(beta, current_eval)
        return current_eval, best_move

# function to make moves in the game
def make_move_RBgame(red, blue, firstplayer="Computer", depth=0):
    current_turn = firstplayer.capitalize()
    print(f"Num red: {red}")
    print(f"Num blue: {blue}")
    print(f"First player: {current_turn}")
    print(f"Depth: {depth}")

    while not (red == 0 or blue == 0):
        # if it's human's turn, get input for the move
        if current_turn == "Human":
           
            print(f"Red: {red}")
            print(f"Blue: {blue}")
            pile = input("Enter pile (red/blue): ")
            print(f"You removed 1 from the {pile} pile.")
            if pile == 'red':
                red = red - 1
                last_move = ("red", 1)
            else:
                blue = blue - 1
                last_move = ("blue", 1)
            current_turn = "Computer"
            # if it's computer's turn, use min-max algorithm to make the best move
        else:
            print(f"Red: {red}")
            print(f"Blue: {blue}")
            best_score = float('-inf')
            chosen_move = None
            for move in best_possible_moves(red, blue):
                store = minmax_alphabetaprune(move[0], move[1], depth - 1)
                current_eval, chosen_moveion = store[0], store[1]
                if current_eval >= best_score:
                    best_score = current_eval
                    chosen_move = move

            if chosen_move[0] == red - 1:
                print("The computer removed 1 from the red pile.")
                red = red - 1
                last_move = ("red", 1)
            elif chosen_move[1] == blue - 1:
                print("The computer removed 1 from the blue pile.")
                blue = blue - 1
                last_move = ("blue", 1)
            current_turn = "Human"
    
    # congratulate the winner
    if current_turn == "Human":
        print(f"Game over. \nCongratulations! You won with a score of {eval_func(red, blue)}.")
    else:
        print(f"Game over. \nBetter luck next time! The computer won with a score of {eval_func(red, blue)}.")

                
def main():
      # Parse command line arguments
    red = int(sys.argv[1]) # Number of red stones in the pile
    blue = int(sys.argv[2]) # Number of blue stones in the pile
    firstplayer = sys.argv[3] if len(sys.argv) >= 4 else 'computer' # The player who moves first
    depth = int(sys.argv[4]) if len(sys.argv) >= 5 else 3 # The depth of the Minimax algorithm
    # Call the make_move_RBgame function to play the game
    make_move_RBgame(red,blue,firstplayer,depth)

main()
