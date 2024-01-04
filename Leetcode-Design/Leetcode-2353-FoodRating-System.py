from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cusines_food = defaultdict(SortedSet)
        self.cusines = {}
        self.ratings = {}
        for i in range(len(foods)):
            self.cusines_food[[cuisines[i]]].add((-ratings[i], foods[i]))
            self.cusines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cusines[food]
        r = self.ratings[food]
        self.cusines_food[c].remove((-r, food))
        self.cusines_food[c].add((-newRating, food))
        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cusines_food[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)