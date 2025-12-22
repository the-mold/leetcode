class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
  
  def swap(self, index_1, index_2):
    self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
  
  def sift_up(self, index):
    current_index = index
    while current_index > 0:
      # formula to fine parent
      parent_index = (current_index - 1) // 2
      if self.list[current_index] < self.list[parent_index]:
        self.swap(current_index, parent_index)
        current_index = parent_index
      else:
        break
    
  def insert(self, val): #T:O(log n)
    self.list.append(val)
    self.sift_up(self.size() - 1) #T:O(log n)

  def sift_down(self, curr_idx):
    while curr_idx < self.size() - 1:
      # formula to find left child
      left_child_idx = 2*curr_idx + 1
      # formula to find right child
      right_child_idx = 2*curr_idx + 2

      left_child_val = self.list[left_child_idx] if left_child_idx < self.size() else float("inf")
      right_child_val = self.list[right_child_idx] if right_child_idx < self.size() else float("inf")

      # select the smaller of two children
      smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
      smaller_child_idx = left_child_idx if left_child_val < right_child_val else right_child_idx
      
      # swap parent with the lesser one
      if self.list[curr_idx] > smaller_child_val:
        self.swap(curr_idx, smaller_child_idx)
        curr_idx = smaller_child_idx
      else:
        break
    
  def extract_min(self): #T:O(log n)
    if self.is_empty():
      return None

    if self.size() == 1:
      return self.list.pop()
      
    res = self.list[0]
    # reassign the last element to the start
    self.list[0] = self.list.pop()
    # now move the new root down to proper position
    self.sift_down(0) #T:O(log n)

    return res

# Time
# extract_min(self): #T:O(log n)
# insert(self, val): #T:O(log n)
