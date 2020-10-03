class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = []
        n2 = []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        n1.reverse()
        n2.reverse()
        res = int(''.join(map(str,n1))) + int(''.join(map(str,n2)))
        ans = l1 = ListNode(res%10)
        res //= 10
        while res:
            l1.next = ListNode()
            l1.next.val = res%10
            res //= 10
            l1 = l1.next
        return ans