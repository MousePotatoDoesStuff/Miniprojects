import heapq
from typing import List

class Cuisine:
    def __init__(self):
        self.byRating: dict = dict()
        self.byFood: dict = dict()
        self.ratings = []

    def clearRatings(self):
        while not self.byRating[-self.ratings[0]]:
            e = -(heapq.heappop(self.ratings))
            self.byRating.pop(e)
        return

    def addRating(self, food, rating):
        if rating in self.byRating:
            S = self.byRating[rating]
            S.add(food)
        else:
            self.byRating[rating] = {food}
            heapq.heappush(self.ratings, -rating)
        self.byFood[food] = rating
        return

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.byFood[food]
        self.byFood[food] = newRating
        self.byRating[oldRating] -= {food}
        self.addRating(food, newRating)
        self.clearRatings()
        return

    def highestRated(self) -> str:
        print(self.byRating)
        if not self.byRating:
            return ""
        e=-self.ratings[0]
        return min(self.byRating[e])

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines={e:None for e in cuisines}
        self.byFood=dict()
        for e in self.cuisines:
            self.cuisines[e]=Cuisine()
        for i in range(len(foods)):
            f,c,r=foods[i],cuisines[i],ratings[i]
            C:Cuisine=self.cuisines[c]
            C.addRating(f,r)
            self.byFood[f]=C
        return

    def addRating(self, food, rating):
        cuisine=self.byFood[food]
        cuisine.addRating(food,rating)
        return

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine=self.byFood[food]
        cuisine.addRating(food,newRating)
        return

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine].highestRated()


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


def main():
    return


if __name__ == "__main__":
    main()
