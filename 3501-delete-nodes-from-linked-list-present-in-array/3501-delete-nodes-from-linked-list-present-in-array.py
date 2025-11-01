# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=ListNode()
        p=ListNode()
        s.next=p
        p.next=head
        nums=set(nums)
        while head:
            if head.val not in nums:
                p=head
            else:
                p.next=head.next
            head=head.next
            
        return s.next.next

        