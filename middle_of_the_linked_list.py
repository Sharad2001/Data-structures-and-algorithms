class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = node = head

        while curr:
            length += 1
            curr = curr.next

        mid = length // 2
        count = 0
        while node:
            if count == mid:
                return node

            else:
                count += 1
                node = node.next
        return None