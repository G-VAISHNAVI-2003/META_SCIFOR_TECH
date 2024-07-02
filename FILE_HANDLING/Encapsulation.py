class Listop:
    def __init__(self, d):
        self._d = d
    
    def get_data(self):
        return self._d
    
    def set_data(self, n_data):
        self._d = n_data
    
    def add_data(self, ele):
        self._d.append(ele)
    
    def remove_data(self, ele):
        if ele in self._d:
            self._d.remove(ele)
        else:
            print("Element not found in the list..")
    
    def sorting_data(self):
        self._d.sort()
    
    def reversing_data(self):
        self._d.reverse()
    
    def get_length(self):
        return len(self._d)
op = Listop([1, 2, 3, 4, 5, 7, 8, 9, 5])

print("Original List:", op.get_data())

op.add_data(10)
print("List after adding 10:", op.get_data())

op.remove_data(7)
print("List after removing 7:", op.get_data())

op.sorting_data()
print("Sorted List:", op.get_data())

op.reversing_data()
print("Reversed List:", op.get_data())

print("Length of the List:", op.get_length())
