class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        days_sett = set(days)
        last_day = days[-1]

        def solve(curr_day):
            if curr_day > last_day:
                return 0
            if curr_day in memo:
                return memo[curr_day]
            
            # if you do not need to travel, just move to the next day
            if curr_day not in days_sett:
                return solve(curr_day + 1)

            one_day_ticket_cost = costs[0] + solve(curr_day + 1)
            seven_day_ticket_cost = costs[1] + solve(curr_day + 7)
            thrity_day_ticket_cost = costs[2] + solve(curr_day + 30)

            res = min(one_day_ticket_cost, min(seven_day_ticket_cost,thrity_day_ticket_cost))
            memo[curr_day] = res
            return res


        # Top down approach: start with the big question: "What is the minimum cost for my entire travel plan, starting from the first day I need to travel?"
        # Breaks it down: To answer this, it recursively breaks the problem into smaller subproblems. For example, to find solve(day_1), it needs to know the answers for solve(day_1 + 1), solve(day_1 + 7), and solve(day_1 + 30).
        return solve(0)