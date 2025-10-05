idx_value_mapping = {
    0: 20,
    1: 50,
    2: 100,
    3: 200,
    4: 500
}
value_idx_mapping = {
    20: 0,
    50: 1,
    100: 2,
    200: 3,
    500:4
}

class ATM:

    def __init__(self):
        self.inventory = {
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0
        }

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, count in enumerate(banknotesCount):
            if count > 0:
                nominal = idx_value_mapping[idx]
                self.inventory[nominal] += count

    def _process_withdraw(self, withdraw_amount, _inventory):
        nominals = [20,50,100,200,500]
        res = [0] * len(nominals)
        amount = withdraw_amount
        for substractor_idx in range(len(nominals) - 1, -1, -1):
            substractor = nominals[substractor_idx]
            count = 0

            while amount >= substractor and _inventory[substractor] > 0:
                amount -= substractor
                _inventory[substractor] -= 1
                count += 1
            
            res[value_idx_mapping[substractor]] = count

        if amount == 0:
            return res

        # all other cases
        return [-1]


    def withdraw(self, amount: int) -> List[int]:
        # dry run
        _inventory = self.inventory.copy()
        res = self._process_withdraw(amount, _inventory)
        if res == [-1]:
            return res

        # real processing
        return self._process_withdraw(amount, self.inventory)

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)