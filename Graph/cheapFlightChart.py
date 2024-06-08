"""
Cheapest Flights Within K Stops
Difficulty: Medium
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, 
return the cheapest price from src to dst with at most k stops. If there is no such route, return -1

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst

Solution (Bellman Ford)
----------
Bellman fords algorithm deals with the negative cycles or negative edges, but time complexity little more than
Dijikstra's. O(E*V), Bellman ford use BFS method to iterate through graph nodes.

Steps
--------
1) Create a main array store the prices of all nodes. And a temp array inside the loop of BFS.
2) Assign source node price as 0 since it is starting point prices[source]. Other values initiate with infinity.
3) Now iterate through every nodes in the give input format 
(since the input order given here sorted from source to destination order)
4) If the source prices are not updated that means the node is not visited yet, if value is "inf" we will point back to
start of the loop.
5) Else we will see source + currentPrice is less than destination price in tempPrice 
(since the tempPrice will be current update point) then we will update with min price 
in tempPrice only, since the other node are reachable only when a stop is covered by flight, 
ie, BFS way from 1st adjacent node to it's next adjacent node in next iteration.
At end of loop itertaion we replace main price with temp price.
6) We have to do the assignation only in tempPrice array. Once the all nodes are traversed once we will do this 
iteration from step 3, until the N times completed usually the node counts (here we take the max stops count).
7) Then atlast return the price[dist], if price[dist] is still "inf" , return -1.
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for stop in range(k+1):
            tempPrice = prices.copy()
            for source, dest, connectprice in flights:
                if prices[source] == float('inf'):
                    continue
                calculatedPrice = prices[source] + connectprice
                if calculatedPrice < tempPrice[dest]:
                    tempPrice[dest] = calculatedPrice
            prices = tempPrice
                
        return -1 if prices[dst] == float("inf") else prices[dst]

# Testing
sol = Solution()
print(sol.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))