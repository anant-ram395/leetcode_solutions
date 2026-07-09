class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1_count={}
        window={}
        for ch in s1:
            s1_count[ch]=s1_count.get(ch,0)+1
        left=0
        for right in range(len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            while right-left+1>len(s1):
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if window==s1_count:
                return True
        return False
