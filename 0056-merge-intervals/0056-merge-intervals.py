class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Brute Force Approach
        intervals.sort()
        mergedIntervals = []
        
        ip1 = 0
        ip2 = 1
        mip = 0
        
        
        
        # mergedIntervals.append(intervals[0])
        
#         while ip1 < len(intervals):
#             start, end = intervals[ip1][0], intervals[ip1][1]
#             if not mergedIntervals == [] and end <= mergedIntervals[-1][1]:
#                     continue
#             while ip2 < len(intervals):
#                 if intervals[ip2][0] <= end:
#                     end = max(end, intervals[ip2][1])
#                     ip2 += 1
#                 else:
#                     break
                    
#             mergedIntervals.append([start, end])
#             ip1 += 1
#             ip2 = ip1+1
#                     # if intervals[ip1][0] > mergedIntervals[mip][1]:
#                     #     mergedIntervals.append(intervals[ip1])
#                     #     mip += 1

            
            
#         print(mergedIntervals)

        n = len(intervals)
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            if not mergedIntervals == [] and end <= mergedIntervals[-1][1]:
                continue
            for j in range(i+1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            mergedIntervals.append([start, end])
            
            



        
        return mergedIntervals