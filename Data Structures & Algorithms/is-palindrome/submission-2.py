import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_list = re.sub(r'[^A-Za-z0-9]', '', s).lower()


        l_ptr = 0
        r_ptr = len(cleaned_list)-1

        while(l_ptr < r_ptr):
            if(cleaned_list[l_ptr] != cleaned_list[r_ptr]):
                return False
            l_ptr += 1
            r_ptr -= 1

        return True