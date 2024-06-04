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
#         n = len(intervals)
#         for i in range(n):
#             # start = intervals[i][0]
#             # end = intervals[i][1]
            
#             if mergedIntervals == []:
#                 mergedIntervals.append(intervals[i])
#             if intervals[i][0] <= mergedIntervals[-1][1]:
#                 mergedIntervals[-1][1] = max(mergedIntervals[-1][1], intervals[i][1])
#             else:
#                 mergedIntervals.append(intervals[i])
            
            

            
        # intervals.sort()
        n = len(intervals)
        temp = n
        
        #for i in range(len(intervals) - 3):
        i = 0
        while i<temp-1:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][0] <= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max([intervals[i][1], intervals[i+1][1]])]
                del intervals[i+1]
            if temp == len(intervals):
                i += 1
            temp = len(intervals)
        print(intervals)
        
        return intervals


        
        # return mergedIntervals