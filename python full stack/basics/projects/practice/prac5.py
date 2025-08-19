'''You have received a list of words, each with a number embedded indicating how many times
that word should be repeated. Your task is to construct a new string by repeating each word the
specified number of times. For example, the word "hello3" should be repeated 3 times. Can you
generate the final string based on this pattern?
Constraints:
● The number of words is 1≤n≤100.
● Each word contains exactly one number indicating how many times it should be
repeated.
Sample Input:
["hello3", "world2"]
Sample Output:
"hellohellohello worldworld"
Explanation:
"hello3" repeats "hello" 3 times, and "world2" repeats "world" 2 times.'''
l=list(input().split())
for i in l:
    print(i[:-1]*int(i[-1]),end=" ")
