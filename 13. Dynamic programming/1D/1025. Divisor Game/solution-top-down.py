class Solution:
    def divisorGame(self, n: int) -> bool:
        # memo[k] will store whether k is a winning number (True) or losing number (False).
        memo = {}

        def is_winning_number(k: int) -> bool:
            # The player who gets 1 loses immediately. So, 1 is a "losing number".
            if k == 1:
                return False
            
            # If we already figured this number out, just return the answer.
            if k in memo:
                return memo[k]
            
            # --- Try to find a winning move ---
            # A winning move is one that leaves the opponent with a losing number.
            
            # Check all valid moves (x is a divisor of k).
            for x in range(1, k):
                if k % x == 0:
                    # 'next_number' is what the opponent will get.
                    next_number = k - x
                    
                    # We ask: "Is this next_number a losing one for them?"
                    # We find out by calling is_winning_number(next_number).
                    # If it returns False, it means they lose from there.
                    if not is_winning_number(next_number):
                        # We found a move that forces a win!
                        # So, 'k' is a winning number.
                        memo[k] = True
                        return True
            
            # If we looped through all possible moves and none of them
            # could force a loss on the opponent, then 'k' must be a losing number.
            memo[k] = False
            return False

        # Alice wins if the starting number 'n' is a winning number.
        return is_winning_number(n)



# Step-by-Step Trace for is_winning_number(3)
# The call stack grows downwards and resolves upwards.

# is_winning_number(3) is called.
# k=3. It's not 1.
# 3 is not in memo.
# It starts the for loop to find divisors of 3.
# x=1: 3 % 1 == 0 is true. This is a valid move.
# The next_number for the opponent will be 3 - 1 = 2.
# Now, it must check if 2 is a losing number for the opponent by calling is_winning_number(2).

# is_winning_number(2) is called.
# k=2. It's not 1.
# 2 is not in memo.
# It starts the for loop to find divisors of 2.
# x=1: 2 % 1 == 0 is true. This is a valid move.
# The next_number for the opponent will be 2 - 1 = 1.
# Now, it must check if 1 is a losing number by calling is_winning_number(1).

# is_winning_number(1) is called.
# k=1. It hits the base case if k == 1: return False.
# It returns False. This means 1 is a "losing number".

# Back to is_winning_number(2):
# The recursive call is_winning_number(1) returned False.
# The condition if not is_winning_number(next_number): becomes if not False:, which is True.
# This means it found a winning move! (By giving the opponent the number 1).
# It executes step 5:
# memo[2] = True (stores that 2 is a winning number).
# It returns True.

# Back to is_winning_number(3):
# The recursive call is_winning_number(2) returned True.
# The condition if not is_winning_number(next_number): becomes if not True:, which is False.
# This means the move x=1 does not lead to a win, because it gives the opponent a winning number (2).
# The loop continues to check for other divisors of 3.
# x=2: 3 % 2 == 0 is false. Not a valid move.
# The loop finishes. No winning move was found.
# It executes step 6:
# memo[3] = False (stores that 3 is a losing number).
# It returns False.
# Final Result
# The initial call to is_winning_number(3) returns False. This means Alice loses if the game starts with n=3.

# The memo cache at the end of the process looks like this: {1: False, 2: True, 3: False} (Note: 1 is never stored because it's a base case, but it behaves as False).
