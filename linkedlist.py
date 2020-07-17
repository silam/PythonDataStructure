"""
https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5
lucidprogramming

git add .
git commit -m"..."
git push -u origin master 
silam
Hen89&67Jun09

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def len_iterative(self):
        curr_node = self.head
        len = 0
        while curr_node:
            len += 1
            curr_node = curr_node.next
        return len

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


    def delete_node(self, data):

        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node .next = None
            return
        
        prev_node = None

        while curr_node and curr_node.data != data:
            
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return
        

        prev_node.next = curr_node.next
        curr_node.next = None


    def delete_node_at_position(self, pos):

        curr_node = self.head

        if pos == 0:
            self.head = curr_node.next
            curr_node.next = None
            return
        prev_node = None

        count = 1

        while curr_node and  count != pos:

            prev_node = curr_node
            curr_node = curr_node.next

            count += 1
        if curr_node is None:
            return
        
        prev_node.next = curr_node.next
        curr_node.next = None

    def swap_nodes(self, key_1, key_2):

        
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        #print(prev_1.data)
        #print(curr_1.data)

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        #print(prev_2.data)
        #print(curr_2.data)

        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next




    def reverse_iterative(self):
        prev = None
        curr = self.head

        #A->B->C->D -> none

        while curr:
            nxt = curr.next
            curr.next = prev    
            prev = curr
            curr = nxt
        self.head = prev



    def reverse_recursive(self):

        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev    
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)


        self.head = _reverse_recursive(curr = self.head, prev = None)


    def merged_sorted_2(self, llist):
        p = self.head
        q = llist.head
        s = None
        new_head = None

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q 
                q = s.next
            new_head = s 

        while p and q:

            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not q:
            s.next = p 
        if not p:
            s.next = q 

        return new_head


    

   









    def merge_sorted(self, llist):
        S = LinkedList()
        p = self.head
        q = llist.head

        if not p:
            return q
        if not q:
            return p 
        
        while p and q:
            
            if p.data < q.data:
                print(p.data)
                if S:
                    S.append(p.data)
                    S.next = p

                p = p.next
            else:
                print(q.data)
                if S:
                    S.append(q.data)
                    S.next = q

                q = q.next


        while p:
            S.append(p.data)
            S.next = p
            p = p.next



        while q:
            S.append(q.data)
            S.next = q
            q = q.next
        
        print ("====Merge sorted llists==")
        S.print_list()
        

    def remove_duplicates(self):

        def Contains(q, p):

            if not q:
                return 0

            print ("\nInside contain P " , p.data)
            print ("Inside contain q ", q.data)
            while q:
               
                if q.data == p.data:
                    print ("contain same ", q.data)

                    return 1
                else:
                    print ("contain diff " , q.data)

                    q = q.next
            return 0


        s = LinkedList()
               

        p = self.head
        
        if not p.next:
            return s

        new_head = None

            
        s.append(p.data)
        s.next = None
        

        while p:
            p = p.next
            while p and Contains(new_head, p) == 0:
                if not s.next:
                    s.append(p.data)
                    s.next = None
                    new_head = s.head
                
              
                         
        
        return new_head
        

            



llist1 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(5)
llist1.append(9)


llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)
llist2.append(8)

S = LinkedList()
#llist1.merged_sorted_2(llist2)
llist1.remove_duplicates()



#llist.reverse_recursive()

#llist.print_list()

#print(llist.len_iterative())
#print(llist.len_recursive(llist.head))

#llist.swap_nodes("B", "B")
#llist.delete_node("C")
#print("Swap")

#llist.print_list()