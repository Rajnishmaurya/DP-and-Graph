# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        cycle={}

        while temp:
            if temp in cycle:
                return True
            cycle[temp]=True
            temp=temp.next
        return False

        