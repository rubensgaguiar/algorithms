# 121. Best Time to Buy and Sell Stock

## Statement
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### Example 1
Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2
Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

### Constrains
- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104

## Solution

Consider this case:

---

max_price = 0

- Iteration 1

[(7),1,5,3,6,4]

min = 7

() - min = 0 => max_price = 0

- Iteration 2

[7,(1),5,3,6,4]

min = 1

() - min = 0 => max_price = 0

- Iteration 3

[7,1,(5),3,6,4]

min = 1

() - min = 5 - 1 = 4 => max_price = 4

- Iteration 4

[7,1,5,(3),6,4]

min = 1

() - min = 3 - 1 = 2 => max_price = 4

- Iteration 5

[7,1,5,3,(6),4]

min = 1

() - min = 6 - 1 = 5 => max_price = 5

- Iteration 6

[7,1,5,3,6,(4)]

min = 1

() - min = 4 - 1 = 3 => max_price = 5

---

Another case:

---

max_price = 0

- Iteration 1

[(7),27,5,3,6,4]

min = 7

() - min = 7 - 7 = 0 => max_price = 0

- Iteration 2

[7,(27),5,3,6,4]

min = 7

() - min = 27 - 7 = 20 => max_price = 20

- Iteration 2

[7,(27),5,3,6,4]

min = 7

() - min = 27 - 7 = 20 => max_price = 20

- Iteration 3

[7,27,(5),3,6,4]

min = 5

() - min = 5 - 5 = 0 => max_price = 20

- Iteration 4

[7,27,5,(3),6,4]

min = 3

() - min = 3 - 3 = 0 => max_price = 20

- Iteration 5

[7,27,5,3,(6),4]

min = 3

() - min = 6 - 3 = 3 => max_price = 20

- Iteration 6

[7,27,5,3,6,(4)]

min = 3

() - min = 4 - 3 = 1 => max_price = 20
