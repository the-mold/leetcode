# def missing(arr):
#   arr_s = set(arr)
#   for i in range(len(arr) + 1):
#     if i not in arr_s:
#       return i
    

for i in range(1, 3):
  print("i", i)


def missing(arr):
  act = sum(arr)
  n = len(arr)
  exp = n * (n + 1) / 2
  return exp - act


def twoSum(arr, t):
  arr_s = set(arr)
  for i in range(len(arr) + 1):
    complement = t - arr[i]
    if complement in arr_s and complement != arr[i]:
      return complement, arr[i]
    

def combinelevels(root):
  if not root:
    return []

  result = []
  queue = [root]

  while queue:
    current_values = []
    current_length = len(queue)

    for i in range(current_length):
      node = queue.pop(0)
      current_values.append(node.val)
      
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    result.append(current_values)  

  return result 



def dp(s, wordarr):
  wordarr_s = set(wordarr)
  n = len(s)
  dp = [False] * (n + 1)
  dp[0] = True

  for i in range(1, len(n) + 1):
    for j in range(i):
      if dp[j] and s[j:i] in wordarr_s
        dp[i] = True
        break

  return dp[n]