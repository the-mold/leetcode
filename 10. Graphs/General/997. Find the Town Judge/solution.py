# Intuition: build adjacency array.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 0:
            return -1
        # edge case when there is only one judge in town
        if n == 1 and len(trust) == 0:
            return 1

        trust_to_map = collections.defaultdict(list)
        trust_me_map = collections.defaultdict(list)
        for personThatTrusts, personWhomIstrusted in trust:
            trust_to_map[personThatTrusts].append(personWhomIstrusted)
            trust_me_map[personWhomIstrusted].append(personThatTrusts)

        for key, value in trust_me_map.items():
            if len(value) == n - 1:
                # check condition that the judge trusts nobody
                if key in trust_to_map:
                    continue
                return key

        return -1