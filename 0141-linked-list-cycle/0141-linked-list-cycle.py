# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        
        # while slow != fast and fast.next != None:
        #     slow = slow.next
        #     fast = (fast.next).next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
            
        
        # if fast == None:
        #     return False
        # else:
        #     return True
                
        
        