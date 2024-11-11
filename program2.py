def decode_message(s: str, p: str) -> bool:
    # Initialize DP table with False values
    m, p_len = len(s), len(p)
    dp = [[False] * (p_len + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty message
    dp[0][0] = True
    
    # Handle the case where the pattern starts with one or more '*' that can match an empty string
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  # '*' can match an empty sequence
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # If pattern[j-1] matches s[i-1] or is a '?', carry forward the result
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match 0 characters (dp[i][j-1]) or 1+ characters (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    # The final result is stored in dp[m][p_len]
    return dp[m][p_len]

# Test cases
print(decode_message("aa", "a"))  # False
print(decode_message("aa", "*"))  # True
print(decode_message("cb", "?a")) # False
print(decode_message("cb", "?b")) # True
