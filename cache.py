class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def print_node(self):
        print(self.value)

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
    def print_list(self):
        if self.head == None:
            print("Nothing here")
        else:
            curr = self.head
            while curr != None:
                print(curr.value, "-->", end=" ")
                curr = curr.next
            print()


class _cache:
    def __init__(self, max_size, eviction_policy):
        self.cache_map = {}
        self.cache_list = LinkedList()
        self.max_size = max_size
        self.eviction_policy = eviction_policy
    
    def print_ll(self):
        self.cache_list.print_list()
    
    def print_map(self):
        print(self.cache_map)
    
    def element_eviction(self, eviction_policy):
        # Evict the element basis eviction policy
        temp_node = Node()
        temp_node.value = (None, None)
        if eviction_policy == "LRU":
            if self.cache_list.head:
                temp_node = self.cache_list.head
                # removing node from linked list and assigning head to the next node
                self.cache_list.head = (self.cache_list.head).next
                if (self.cache_list.head):
                    (self.cache_list.head).prev = None

        # fetching the key from the temp node
        key_to_be_removed = temp_node.value[0]
        if key_to_be_removed:
            self.cache_map.pop(key_to_be_removed)
            print("key " + str(key_to_be_removed) + " removed from the cache as per eviction policy")
        else:
            print("Nothing to be removed")        

    
    def insert_element_in_cache(self, key, value):
        new_node = Node((key,value))
        # print(new_node.value)

        if (self.cache_list.head == None) or (self.cache_list.head.value == None):
            self.cache_list.head = new_node
            self.cache_list.tail = new_node
        else:
            new_node.prev = self.cache_list.tail
            self.cache_list.tail.next = new_node
            self.cache_list.tail = new_node

        self.cache_map[key] = self.cache_list.tail



    def put(self, key, value):
        print("putting "+ key + " into cache")
        if len(self.cache_map) >= self.max_size:
            print("inside if")
            # eviction the value as per the set eviction policy
            # put the element into cache after eviction
            self.element_eviction(self.eviction_policy)
        print("inserting initiated for "+ key + " into cache")   
        self.insert_element_in_cache(key, value)
        print("inserted key "+ key + " into cache")

    def get(self, key):
        if self.cache_map.get(key):
            candidate_node = self.cache_map.get(key)

            # LRU --> accessed node needs to be moved to the last
            
            if candidate_node != self.cache_list.tail:

                if candidate_node == self.cache_list.head:
                    self.cache_list.head = candidate_node.next
                
                elif candidate_node.prev:
                    (candidate_node.prev).next = candidate_node.next
                    (candidate_node.next).prev = candidate_node.prev

                self.cache_list.tail.next = candidate_node
                candidate_node.prev = self.cache_list.tail
                candidate_node.next = None
                
                self.cache_list.tail = candidate_node
                
                self.cache_map[key] = self.cache_list.tail
            
            return candidate_node.value[1]
        
        return None


if __name__ == "__main__":
   demo_cache = _cache(1, "LRU")
   demo_cache.put("a", 1)
   demo_cache.put("b", 5)
   demo_cache.put("c", 9)
   demo_cache.put("d", 15)
   demo_cache.put("e", 23)
   demo_cache.print_ll()
   demo_cache.print_map()

   print(demo_cache.get("a"))
   demo_cache.print_ll()
   demo_cache.print_map()

   print(demo_cache.get("d"))
   demo_cache.print_ll()
   demo_cache.print_map()

   demo_cache.put("f", 55)
   demo_cache.print_ll()
   demo_cache.print_map()