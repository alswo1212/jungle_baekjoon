class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            return list1 if list2 == None else list2
        
        result = list1 if list1.val <= list2.val else list2
        if result == list1:
            list1 = list1.next
        else :
            list2 = list2.next
        
        temp = result
        while (list1 != None or list2 != None) and temp != None:
            if list1 == None or list2 == None:
                if list1 == None:
                    temp.next = list2
                    list2 = list2.next
                elif list2 == None:
                    temp.next = list1
                    list1 = list1.next
                temp = temp.next
                continue
            
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else :
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        return result