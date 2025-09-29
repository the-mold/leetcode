def asteroidCollision(asteroids: list[int]) -> list[int]:
  stack = []

  for ast in asteroids:
      destroyed = False

      while stack and ast < 0 < stack[-1]:
          ast_abs = abs(ast)
          if stack[-1] == ast_abs: #both asteroids explode
              stack.pop()
              destroyed = True
              break
          elif stack[-1] > ast_abs:
              destroyed = True
              break
          else: #previous asteroid explodes. Continue to the next one on the left
              stack.pop()

      if not destroyed:
          stack.append(ast)

  return stack

#T:O(n)
#S:O(n)

# Time is linear O(n) because each asteroid is pushed onto the stack once and popped at most once.
# That means:
# Even if the while loop is nested, an asteroid can cause another to pop only once.
# So, for n asteroids:
# You push at most n items to the stack.
# You pop at most n items from the stack.