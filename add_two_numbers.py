from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Dummy head simplifies the creation of the new linked list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # Continue looping as long as there are nodes to process or a carry left over
    while l1 is not None or l2 is not None or carry > 0:
        # Get the current values if the nodes exist, otherwise use 0
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        
        # Calculate the total and the new carry
        total = val1 + val2 + carry
        carry = total // 10  # Integer division gets the tens digit (e.g., 15 // 10 = 1)
        
        # Create a new node with the ones digit and attach it to our result list
        current.next = ListNode(total % 10)
        current = current.next
        
        # Move forward in both lists if possible
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
            
    return dummy_head.next

# --- Test Cases ---
if __name__ == "__main__":
    # Helper function to convert a Python list to a Linked List
    def to_linked_list(lst: list) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    # Helper function to convert a Linked List back to a Python list
    def to_python_list(node: Optional[ListNode]) -> list:
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res








    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
    ]
    
    for i, (list1, list2, expected) in enumerate(test_cases, 1):
        l1 = to_linked_list(list1)
        l2 = to_linked_list(list2)
        
        result_node = addTwoNumbers(l1, l2)
        result_list = to_python_list(result_node)
        
        status = "PASSED" if result_list == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"  Input:    l1 = {list1}, l2 = {list2}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result_list}\n")