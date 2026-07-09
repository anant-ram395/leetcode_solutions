class Solution(object):
    def characterReplacement(self, s, k):
        count={}
        left=0
        maxf=0
        longest=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxf=max(maxf,count[s[right]])
            while (right-left)+1-maxf>k:
                count[s[left]]-=1
                left+=1
        longest=max(longest,right-left+1)
        return longest

        