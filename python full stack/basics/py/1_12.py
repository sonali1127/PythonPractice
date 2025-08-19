def minimum_cost_to_form_string(n, substrings, main_string):
    main_len = len(main_string)
    dp = [float('inf')] * (main_len + 1)
    dp[0] = 0  # Base case: cost to form an empty prefix is 0

    for i in range(1, main_len + 1):
        for substring, cost in substrings:
            sub_len = len(substring)
            if i >= sub_len and main_string[i - sub_len:i] == substring:
                dp[i] = min(dp[i], dp[i - sub_len] + cost)

    return dp[main_len] if dp[main_len] != float('inf') else "Impossible"

# Input Handling
n = int(input())
substrings = []
for _ in range(n):
    substring, cost = input().split()
    substrings.append((substring, int(cost)))
main_string = input()

# Output the result
a=minimum_cost_to_form_string(n, substrings, main_string)
print(int(a))
