'''Two friends, Alice and Bob, were given two strings and challenged to check if one is a
permutation of the other. Alice insists that a permutation should contain the same characters but
in a different order. Bob, on the other hand, is skeptical. Can you help them by determining if
one string is a permutation of the other?
Constraints:
● The length of both strings is 1≤n≤10^5.
● The strings consist of uppercase and lowercase English alphabets.
Sample Input:
"abc", "cab"
Sample Output:
True
Explanation:
Both strings contain the same characters in different orders, so they are permutations of each
other.'''
a=input()
b=input()
if sorted(a)==sorted(b):
    print("True")
else:
    print("False")
# c=0
# # for i in a:
# #     if i not in b:
# #         print("False")
# #         c=c+1
# #         break
# # if c==0:
# #     print("True")