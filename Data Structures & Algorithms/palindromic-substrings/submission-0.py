class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expand_around_center(left: int, right: int) -> int:
            palindromes = 0
            # Expand outward as long as indices are valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1
            return palindromes

        # Try every index as a center
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            count += expand_around_center(i, i)
            # Even-length palindromes (two-character center)
            count += expand_around_center(i, i + 1)
            
        return count