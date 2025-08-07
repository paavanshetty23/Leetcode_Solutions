class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)!=len(t):
        return False

      maps = {}
      mapt={}

      for i in s:
        maps[i]=maps.get(i,0)+1

      
      for i in t:
        mapt[i]=mapt.get(i,0)+1

     
      return maps==mapt

