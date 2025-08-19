'''In a world where magical creatures live in harmony, every creature has a unique power level
represented by an array. However, to determine the total power, each creature wants to know
the total power of all others except itself. Can you calculate the product of all numbers in the
array except the current one for each index, without using division? The creatures will be very
grateful if you can solve this for them.
Constraints:
● The length of the array is 1≤n≤10^5.
● Each number in the array is between 1≤num≤ 10^4.
Sample Input:
[1, 2, 3, 4]
Sample Output:
[24, 12, 8, 6]
Explanation:
For the first index, the product of all other numbers is 2×3×4=242 \times 3 \times 4 = 24.
Similarly, for the second index, it's 1×3×4=121 \times 3 \times 4 = 12, and so on.
'''
l=list(map(int,input().split()))
d=[]
m=1
for i in l:
    m=m*i
for i in l:
    res=m//i
    d.append(res)
print(d)
    