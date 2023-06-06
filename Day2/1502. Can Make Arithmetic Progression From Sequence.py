// Brute Force

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = abs(arr[1]-arr[0])
        
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1]!=diff:
                return False
        return True



// Intutitive Solution

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        length = len(arr)
        min_value = 1000000
        max_value = -1000000

        for value in arr:
            if value<min_value:
                min_value = value
            if value>max_value:
                max_value = value
        
        d = (max_value - min_value)/ (length-1)
        
    
        for i in range(length):
            if min_value+i*d not in arr:
                return False

        return True


