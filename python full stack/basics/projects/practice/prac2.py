'''Problem Statement:
Alice is attending a cryptography class and has discovered that anagrams can be very useful.
She is working on an encryption scheme that involves two large strings. The encryption is
dependent on determining the minimum number of character deletions required to turn the
two strings into anagrams.
Two strings are considered anagrams if the letters of one string can be rearranged to form the
other string, meaning both strings must contain the same exact letters in the same exact
frequencies.
Given two strings, your task is to calculate the minimum number of deletions required to make
them anagrams. Characters can be deleted from either string.
Constraints:
● Both strings consist only of lowercase English letters (a to z).
● The lengths of the strings can vary but will not exceed ten to the power of four.
Input Format:
● The first line contains the first string.
● The second line contains the second string.
Output Format:
● Print a single integer denoting the minimum number of character deletions required to
make the strings anagrams.
Sample Input
cde
abc
Sample Output:
4
Explanation:
To make the strings anagrams:
● Remove d and e from "cde" to get "c".
● Remove a and b from "abc" to get "c".
This results in a total of 4 deletions.
'''
a=input()
b=input()
c=0
for i in a:
    if i not in b:
        c=c+1
for i in b:
    if i not in a:
        c=c+1
print(c)