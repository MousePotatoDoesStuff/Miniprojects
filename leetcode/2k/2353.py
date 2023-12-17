class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.byRating = dict()
        self.byFood = dict()
        self.ratings = []

    def clearRatings(self):
        while not self.byRating[self.ratings[0]]:
            e = heapq.heappop(self.ratings)
            self.byRating.
        return

    def addRating(self, food, rating):
        if rating in self.byRating:
            S = self.byRating[rating]
            heapq.heappush(S, food)
        else:
            self.byRating[rating] = [food]
            heapq.heappush(self.ratings, rating)
        self.byFood[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.byFood[rating]

    def highestRated(self, cuisine: str) -> str:


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


def main():
    return


if __name__ == "__main__":
    main()
