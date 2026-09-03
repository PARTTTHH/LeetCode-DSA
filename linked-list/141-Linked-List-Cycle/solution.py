
# Floyd's Cycle Detection (two pointers)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = head
        end = head

        while end and end.next:
            start = start.next
            end = end.next.next

            if start == end:
                return True

        return False


# SET BASED 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tracker = set()
        curr = head

        while curr:
            if curr in tracker:
                return True

            tracker.add(curr)

            curr = curr.next

        return False