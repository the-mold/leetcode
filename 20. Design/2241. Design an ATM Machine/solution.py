class ATM:

    def __init__(self):
        self.denominations = [20,50,100,200,500]
        self.inventory = [0] * len(self.denominations)

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, count in enumerate(banknotesCount):
            self.inventory[idx] += count

    def withdraw(self, amount: int) -> List[int]:
        withdrawal_plan = [0] * len(self.denominations)
        remaining_amount = amount

        for i in range(len(self.denominations) - 1, -1, -1):
            denomination_value = self.denominations[i]
            notes_available = self.inventory[i]

            # Determine the number of notes to use for the current denomination.
            # It's the minimum of what's available and what's needed for the remaining amount.
            notes_to_dispense = min(remaining_amount // denomination_value, notes_available)

            # Update the plan and the remaining amount.
            withdrawal_plan[i] = notes_to_dispense
            remaining_amount -= notes_to_dispense * denomination_value
        
        if remaining_amount == 0:
            for idx, count in enumerate(withdrawal_plan):
                self.inventory[idx] -= count

            return withdrawal_plan
        else:
            return [-1]
        
# Time Complexity
# __init__(): O(1)
# Initialization involves creating two lists of a fixed size (5). This is a constant-time operation.
# deposit(): O(1)
# The method loops exactly 5 times to update the banknote counts. Since the number of iterations is constant and does not depend on any input size, the complexity is constant.
# withdraw(): O(1)
# This method also uses a loop that runs exactly 5 times (from the largest to the smallest denomination).
# All operations inside the loop (arithmetic, comparisons) are constant time.
# The final loop to update the counts (if the withdrawal is successful) also runs 5 times.
# Because the number of operations is always fixed regardless of the amount or the number of banknotes in the machine, the time complexity is constant.
# Space Complexity
# Overall Space: O(1)
# The ATM class stores two lists (denominations and banknotes), both of a fixed size (5). The space required does not grow with the number of operations or the size of the deposits/withdrawals.
# Auxiliary Space (per method call):
# deposit(): O(1). It modifies the existing banknotes list in place and uses no extra space.
# withdraw(): O(1). It creates a temporary withdrawal_plan list of a fixed size (5). The space used does not scale with the input amount.