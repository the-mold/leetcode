# Suffix trie: for each entry and for each suffix of the entry you fill up trie starting from the root.
# In this way all possible search combinations are available starting from the root of the trie.

class TrieNode:
  def __init__(self):
    self.children = {}
    # save index of each log entry where a node was seen
    self.indexes = set()
    

class TrieLogs:
  def __init__(self):
    self.root = TrieNode()
    self.log_entries = []
    
  def process_logs(self, logs):
    for log_idx, line in enumerate(logs):
      self._process_log_line(line, log_idx)

  def _process_log_line(self, log_line, log_idx):
    self.log_entries.append(log_line)
    
    for i in range(len(log_line)):
      node = self.root
      
      # for each suffix create a separate chain of entries starting from the root.
      # For example: For the log entry: "the quick brown fox"
      # i:0 -> "the quick brown fox"
      # i:1 -> "he quick brown fox"
      # i:2 -> "e quick brown fox"
      #...
      suffix = log_line[i:]
      
      for ch in suffix:
        if ch not in node.children:
          node.children[ch] = TrieNode()
      
        node = node.children[ch]
        
        node.indexes.add(log_idx)
        
  def search(self, phrase):
    node = self.root
    
    for ch in phrase:
      if ch not in node.children:
        return []
    
      node = node.children[ch]
      
    matching_ids = node.indexes
    
    return [self.log_entries[idx] for idx in matching_ids]
    
    
    
      
  
if __name__ == "__main__":
  logs = [
    "the quick brown fox",
    "the slow brown cow",
    "to be or not to be that is the question",
    "bar foo bar barfoo",
  ]
  
  tr = TrieLogs()
  tr.process_logs(logs)
  
  # searcg
  search_queries = [
    "brown",
    "the question",
    "bla no match"
  ]
  
  for q in search_queries:
    print(tr.search(q))
  