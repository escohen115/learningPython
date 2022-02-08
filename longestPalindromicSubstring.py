class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

#         psuedo code non optimal solution
#         how to check if a string is a palindrome

#         iterate through every letter
#         after every new letter added to the word, check if the reverse is the same as forwards

        longest = ""
        for i in range(len(s)):
            buildup = s[i]
            if buildup[::-1] == buildup and len(buildup) > len(longest):
                longest = buildup
            for j in range(i+1, len(s)):
                buildup += s[j]
                # print(buildup)
                if buildup[::-1] == buildup and len(buildup) > len(longest):
                    longest = buildup
        return longest
