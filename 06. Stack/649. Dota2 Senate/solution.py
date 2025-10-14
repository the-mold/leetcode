class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_dq, d_dq = deque(), deque()

        # fill up both queues
        for idx, ch in enumerate(senate):
            if ch == "R":
                r_dq.append(idx)
            else:
                d_dq.append(idx)

        # simulate voting
        while r_dq and d_dq:
            r = r_dq.popleft()
            d = d_dq.popleft()
            # priority has voter with lower index because he votes first and can ban the other one.
            if r < d:
                # once voter banned another one, put him back in stack. He is still there, but he can not easily be banned by any subsequent voter from another party, hence r + n to make his value as low as possible.
                r_dq.append(r+n)
            else:
                d_dq.append(d+n)
        
        return "Radiant" if r_dq else "Dire"

        