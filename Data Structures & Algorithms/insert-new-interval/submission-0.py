class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n, output = 0, len(intervals), []

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1],newInterval[1])]
            i += 1
        output.append(newInterval)
        
        while i < n:
            output.append(intervals[i])
            i += 1
            
        return output