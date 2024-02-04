class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        separator = " -> "
        while current:
            print(current.data, end=separator if current.next else "\n")
            current = current.next

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        cur = self.head

        while cur:
            next_node = cur.next
            sorted_head = self.sorted_insert(sorted_head, cur)
            cur = next_node

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        cur = sorted_head
        while cur.next and cur.next.data < new_node.data:
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node
        return sorted_head

    def merge_sorted_lists(self, llist1, llist2):
        dummy_head = Node()
        current = dummy_head

        while llist1 and llist2:
            if llist1.data < llist2.data:
                current.next = Node(llist1.data)
                llist1 = llist1.next
            else:
                current.next = Node(llist2.data)
                llist2 = llist2.next

            current = current.next

        current.next = llist1 or llist2

        self.head = dummy_head.next


def main():
    # Create linked lists
    llist1 = LinkedList()
    llist1.insert_at_end(2)
    llist1.insert_at_end(4)
    llist1.insert_at_end(6)

    llist2 = LinkedList()
    llist2.insert_at_end(9)
    llist2.insert_at_end(5)
    llist2.insert_at_end(3)

    # Output lists
    print("Output linked list 1:")
    llist1.print_list()

    print("\nOutput linked list 2:")
    llist2.print_list()

    # Reverse the first list
    llist1.reverse_linked_list()
    print("\nReversed linked list 1:")
    llist1.print_list()

    # Sort the second list
    llist1.insertion_sort()
    llist2.insertion_sort()
    print("\nSorted linked list 1:")
    llist1.print_list()
    print("\nSorted linked list 2:")
    llist2.print_list()

    # Combine and sort lists
    llist_merged = LinkedList()
    llist_merged.merge_sorted_lists(llist1.head, llist2.head)
    print("\nA merged and sorted linked list:")
    llist_merged.print_list()


if __name__ == "__main__":
    main()
