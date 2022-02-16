from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = new_head = ListNode(0)
        while head and head.next:
            temp = head.next
            # next run head.val = temp.next
            head.next = temp.next
            # temp.next = head.val, temp.val = head.next
            # if head is [1, 2, 3, 4], temp [2, 1, 3, 4]
            temp.next = head
            pre.next = temp
            pre = head
            head = head.next
        return new_head.next


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def is_equal(self: Optional[ListNode], other: Optional[ListNode]):
    while self and other and self.val == other.val:
        self = self.next
        other = other.next
    if not self and not other:
        return True
    return False


testC = Solution()
if is_equal(testC.swapPairs(lst2link([1, 2, 3, 4])), lst2link([2, 1, 4, 3])):
    print('test1 - Success')
else:
    print('test1 - Fail')

if is_equal(testC.swapPairs(lst2link([])), lst2link([])):
    print('test2 - Success')
else:
    print('test2 - Fail')

if is_equal(testC.swapPairs(lst2link([1])), lst2link([1])):
    print('test3 - Success')
else:
    print('test3 - Fail')
