def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Calculates the length of the longest common subsequence of two strings.

    Args:
        text1: The first string.
        text2: The second string.

    Returns:
        The length of the longest common subsequence.
    """
    m = len(text1)
    n = len(text2)

    # Create a DP table to store lengths of LCSs.
    # dp[i][j] will be the length of LCS of text1[0..i-1] and text2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in a bottom-up fashion.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters at the current positions match
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            # If the characters do not match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value at dp[m][n] contains the length of the LCS for the entire strings.
    return dp[m][n]

# Example Usage:
text1 = "abcde"
text2 = "ace"
print(f"The length of the Longest Common Subsequence is: {longest_common_subsequence(text1, text2)}")

text3 = "abc"
text4 = "def"
print(f"The length of the Longest Common Subsequence is: {longest_common_subsequence(text3, text4)}")
