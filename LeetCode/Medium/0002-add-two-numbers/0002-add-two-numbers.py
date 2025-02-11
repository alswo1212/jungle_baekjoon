class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def node_2_num(node:ListNode) -> int:
            result = 0
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            while stack:
                num = stack.pop()
                result *= 10
                result += num
            return result
            
        num = node_2_num(l1) + node_2_num(l2)
        result = ListNode(val=num % 10)
        target = result
        while num:
            num //= 10
            if num == 0:
                break
            next_node = ListNode(val=num % 10)
            target.next = next_node
            target = next_node
        return result