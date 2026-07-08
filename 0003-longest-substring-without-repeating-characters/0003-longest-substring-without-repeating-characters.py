class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char=set()
        left=0
        longest=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1

            char.add(s[right])
            longest=max(longest,right-left+1)
        return longest

                