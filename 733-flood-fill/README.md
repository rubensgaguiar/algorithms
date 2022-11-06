# 733. Flood Fill

## Statement
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.


### Example 1
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

### Example 2
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation: The starting pixel is already colored 0, so no changes are made to the image.

### Constrains
- m == image.length
- n == image[i].length
- 1 <= m, n <= 50
- 0 <= image[i][j], color < 216
- 0 <= sr < m
- 0 <= sc < n

## Solution
```
"""
Let's consider this case:

1 1 1
1 1 0
1 0 1

If the input pair (sr, sc) = (1, 1), at first step we have:

 1  {2} 1
{2} [2] 0
 1   0  1

Then we have two new pairs: (sr, sc) = (1, 2) and (sr, sc) = (0, 1).

So taking the first pair, we have:

    {2} [2] {2}
     2   2   0
     1   0   1
    
    In the two elements {}, they have no elements connected with different color, so nothing's happen.


So taking the second pair, we have:

     2  2  2
    [2] 2  0
    {2} 0  1

    In the element {}, it have no elements connected with different color, so nothing's happen.

Thus, our algorithm must perform the task showed above, in a recursive way that if the actual element have a 4-directionally connected pixel, this pixel must to be the new center of another flood fill, and so on. The result of this first flood fill must to be used in the flood fill of the next 4-directionally connected pixel.
"""
```