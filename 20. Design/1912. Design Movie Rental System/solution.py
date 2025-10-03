import collections
import sortedcontainers

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {}
        self.available = collections.defaultdict(sortedcontainers.SortedList)
        self.rented = sortedcontainers.SortedList()

        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.available[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        _available = self.available

        if movie not in _available:
            return []

        return [shop for (price, shop) in _available[movie][:5]]
        

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.available[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.rented.discard((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [(shop, movie) for (price, shop, movie) in self.rented[:5]]


# Complexity Analysis
# Time complexity:

# MovieRentingSystem(n, entries) operation: O(nlogn).

# search(movie) operation: O(logn).

# rent(shop, movie) operation: O(logn).

# drop(shop, movie) operation: O(logn).

# report() operation: O(logn).

# Space complexity: O(n).