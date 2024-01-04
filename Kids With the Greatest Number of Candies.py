class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies=max(candies)
        return [(i+extraCandies >= maxcandies) for i in candies]
