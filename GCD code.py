class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1,str2 = str2,str1
        if str2 == str1 :
            return str1
        if str1[:len(str2)] != str2:
            return ""
        return self.gcdOfStrings(str1[len(str2):],str2)
