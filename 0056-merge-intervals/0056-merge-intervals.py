class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Brute Force Approach
        intervals.sort()
        mergedIntervals = []
        

        # Brute Force Approach
        # TC - O(nlogn) + O(2n)
        # n = len(intervals)
        # for i in range(n):
        #     start = intervals[i][0]
        #     end = intervals[i][1]
        #     if not mergedIntervals == [] and end <= mergedIntervals[-1][1]:
        #         continue
        #     for j in range(i+1, n):
        #         if intervals[j][0] <= end:
        #             end = max(end, intervals[j][1])
        #         else:
        #             break
        #     mergedIntervals.append([start, end])
            
            
        # Optimized Approach TC - O(nlogn) + O(n)
        n = len(intervals)
        for i in range(n):
            if mergedIntervals == [] or mergedIntervals[-1][1] < intervals[i][0]:
                mergedIntervals.append(intervals[i])
            # if intervals[i][0] <= mergedIntervals[-1][1]:
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], intervals[i][1])
            # else:
            #     mergedIntervals.append(intervals[i])
            
            
        
        return mergedIntervals