# -*- coding: utf-8 -*-
class SinglyLinkedListNode(object):
    """
    单链表
    由Head结点和一系列后继结点（next）组成
    """
    def __init__(self,val):
        """
        :param val: int
        """
        self.val = val
        self.next = None

class DoublyLinkedListNode(object):
    """
    双向链表
    由Head结点和一系列后继结点（next）以及前驱结点（prev）组成
    """
    def __init__(self,val):
        """
        :param val: int
        """
        self.val = val
        self.next = None
        self.prev = None

def printlist(head):
    ret = []
    if head:
        current = head
        while current:
            ret.append(current.val)
            current = current.next
    return ret

def reverse_list(head):
    """
    :type head: SinglyLinkedListNode
    """
    # 为了保存原单链表，深赋值copy
    current = head
    reverse_head_prev = None
    reverse_head = None
    while current:
        reverse_current = SinglyLinkedListNode(current.val)
        if reverse_head_prev is not None:
            reverse_head_prev.next = reverse_current
        else:
            reverse_head = reverse_current
        current = current.next
        reverse_head_prev = reverse_current
    # print('reverse_head:{}'.format(printlist(reverse_head)))

    if head is None or head.next is None:
        return reverse_head

    prev = None
    while reverse_head:
        # head不断遍历，current和prev表示当前的前后两个结点操作
        current = reverse_head
        reverse_head = reverse_head.next
        current.next = prev
        prev = current
    return prev

def reverse_list_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    p = head.next
    head.next = None
    revrest = reverse_list_recursive(p) # p结点后的先进行逆序然后将head作为最后的结点即可
    p.next = head
    return revrest

def is_sorted(head):
    """
    从小到达排序
    :type head: SinglyLinkedListNode
    """
    if head is None or head.next is None:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True

def merge_two_list(l1, l2):
    ret = cur = SinglyLinkedListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return ret.next

def is_palindrome(head):
    # print('----is_palindrome----in----')
    head_reverse = reverse_list(head)
    # print('head_reverse:{}'.format(printlist(head_reverse)))
    # print('head:{}'.format(printlist(head)))
    while head:
        if head_reverse.val != head.val:
            # print('----is_palindrome----out----')
            return False
        head = head.next
        head_reverse = head_reverse.next
    # print('----is_palindrome----out----')
    return True


if __name__ == '__main__':
    head = SinglyLinkedListNode(3)
    head.next = SinglyLinkedListNode(4)
    head.next.next = SinglyLinkedListNode(4)
    head.next.next.next = SinglyLinkedListNode(3)
    print(printlist(head))
    print(printlist(reverse_list(head)))
    print(is_sorted(head))
    # print(is_sorted(reverse_list(head)))
    print('回文数:{}'.format(is_palindrome(head)))
    # print(printlist(head))
