UTA ID:1002059166
Full Name: Sravan Chandaka  

Programming language Used:Python 


To run the code:

1.Open the terminal and go to the path where the red_blue_nim.py file is saved 
2.In case of mine it is C:\Users\chand\Projects\AI 
3.Run the command as red_blue_nim.py <num_red> <num_blue> <First_player(Computer/human)> <depth> 
4.If <method> and <dump> has no input given it takes default values as a* and false respectively.



Brief explaination of code:

This code is an implementation of the game "Red and Blue Stones". The game starts with two piles of stones, one red and one blue. Players take turns removing one stone from either the red or blue pile until one of the piles is empty. The score is then calculated based on the number of stones each player has remaining. The code uses the Minimax algorithm with alpha-beta pruning to determine the best move for the computer player. The user can run the code in the command line by specifying the number of red and blue stones, the player who moves first, and the depth of the Minimax algorithm.

eval_func(red, blue): This function takes the number of stones in the red and blue piles as input and calculates the score for the current state of the game. The score is calculated as follows: the number of red stones multiplied by 2, plus the number of blue stones multiplied by 3.

best_possible_moves(red, blue): This function generates a list of all possible moves that can be made in the game. It creates a list of moves by iterating over the range of values from 1 to the number of stones in each pile, and creating a move for each combination of red and blue stones.

minmax_alphabetaprune(red, blue, depth, alpha, beta, is_maximizing): This function implements the Minimax algorithm with alpha-beta pruning to determine the best move for the computer player. It takes as input the number of red and blue stones in the piles, the depth of the search tree to explore, and the alpha and beta values for the alpha-beta pruning algorithm. It also takes a boolean flag indicating whether the current player is maximizing or minimizing. The function recursively explores the search tree, evaluating each node and propagating the best score up the tree, while pruning branches that are guaranteed to be suboptimal.

make_move_RBgame(red, blue, firstplayer, depth): This function implements the game logic, taking as input the number of red and blue stones in the piles, the player who moves first, and the depth of the Minimax algorithm. It alternates between the human player and the computer player, prompting the human player to make a move and using the Minimax algorithm to determine the best move for the computer player.

main(): This function parses the command line arguments, which include the number of red and blue stones, the player who moves first, and the depth of the Minimax algorithm, and calls the make_move_RBgame() function to start the game.


EVALUATION FUNCTION:

The evaluation function used in the program is a simple linear combination of the number of red and blue stones remaining in the pile. It calculates the score as follows:

red_score = red * 2
blue_score = blue * 3
score = red_score + blue_score

The intuition behind this scoring is that the computer player should try to maximize the number of blue stones in the pile, as they are worth more points than red stones. However, the computer should also try to minimize the number of red stones in the pile, as they are worth points to the human player.

By giving red stones a lower weight of 2 and blue stones a higher weight of 3, the evaluation function encourages the computer player to prioritize removing blue stones from the pile, while also penalizing it for leaving behind red stones.

While this evaluation function is simple, it provides a reasonable heuristic for guiding the computer player's decision-making in the RB game.