
input = [
  "item 1",
  "item 2",
  "more item 3",
  "last item 4"
]

class TrieNode:
  def __init__(self):
    self.ids = set()
    self.children = {}
  
head = TrieNode()
    
def insert_string(val, idx):
  node = head
  for ch in val:
    if ch not in node.children:
      node.children[ch] = TrieNode()        
    node = node.children[ch]
    node.ids.add(idx)
  
def build():
  for idx, record in enumerate(input):
    for i in range(len(record)):
      substring = record[i:]
      insert_string(substring, idx)
    
build()

def search(target):
  node = head

  for ch in target:
    if ch in node.children:
      node = node.children[ch]
    else:
      return None

  return node.ids

print("test----------")
print(search("item"))
print(search("4"))
print(search(" "))