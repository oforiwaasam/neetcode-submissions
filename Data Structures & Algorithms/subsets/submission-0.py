class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            
            for i in range(len(output)): 
                newList = list(output[i]) 
                newList.append(num) 
                output.append(newList) 

        return output
        