#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        
        
        if (n>m):
            return False 
        i=0
        j=0
        
        while i<n and j<m:
            
            if s[i]==t[j]:
                i=i+1 
            j=j+1 
        
        return (i==n)