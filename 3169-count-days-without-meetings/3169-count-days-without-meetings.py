class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        # Bruteforce
#         daysCal = [0]*days
#         for sc in meetings:
#             for i in range(sc[0]-1, sc[1]):
#                 if daysCal[i] != -1:
#                     daysCal[i] = -1
#                     days -= 1
        

        
#         return days

        nonMeetDays = 0
        events = []
        for meeting in meetings:
            events.append([meeting[0], +1])
            events.append([meeting[1], -1])
            
        events.append([0, 0])
        events.append([days+1, 0])
        
        events = sorted(events)
        print(events)
        
        num_meetings_running = 0
        for i in range(len(events)-1):
            num_meetings_running += events[i][1]
            if num_meetings_running == 0:
                nonMeetDays += max(events[i+1][0] - events[i][0]-1, 0)
                
                
        
        
        return nonMeetDays