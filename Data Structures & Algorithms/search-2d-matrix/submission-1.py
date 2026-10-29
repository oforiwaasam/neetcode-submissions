class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            l, r = row[0], row[-1]
            print(l, r)

            if target == l or target == r:
                return True
            elif target > l and target < r: # may be within here, so perform binary search
                return self.binarySearch(row, target)
        return False

    def binarySearch(self, rowList, target):
        start, end = 0, len(rowList)

        while start <= end:
            mid = start + (end - start) // 2

            if rowList[mid] == target:
                return True
            elif rowList[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
