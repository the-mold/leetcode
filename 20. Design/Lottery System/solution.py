import random

class LotterySystem:
  def __init__(self):
    self.tickets = []
    self.total_amount = 0

  def buy_ticket(self, user_id, amont_dollars):
    amount_cents = int(amont_dollars * 100)

    self.tickets.append((user_id, amount_cents))
    self.total_amount += amount_cents

  def draw_a_winner(self):
    if not self.tickets:
      print("No tickets sold \n")
      return None

    participants = []
    for user_id, amount in self.tickets:
      participants.extend([user_id] * amount)

    winner = random.choice(participants)

    sum_investment = 0
    for user_id, amount in self.tickets:
      if user_id == winner:
        sum_investment += amount

    print(f"Winner is: {winner}, who bough tickets for {sum_investment / 100} \n")
    print(f"Winner's chance of winning was {(sum_investment / self.total_amount) * 100}%")

  def stats(self):
    if not self.tickets:
      return {
        "total_tickets": 0,
        "total_amount": 0,
        "avg_amount": 0,
      }

    total_tickets = len(self.tickets)

    return {
      "total_tickets": total_tickets,
      "total_amount": self.total_amount / 100,
      "avg_amount": (self.total_amount / total_tickets) / 100,
    }


if __name__ == "__main__":
  lottery = LotterySystem()

  lottery.buy_ticket("Alice", 10)
  lottery.buy_ticket("Bob", 25)
  lottery.buy_ticket("Bob", 5)
  lottery.buy_ticket("Sam", 40)

  print("Lottery stats \n", lottery.stats())

  lottery.draw_a_winner()
