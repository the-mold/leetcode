def find_most_frequest_transition(logs):
  last_visited_page_by_user = {}
  transitions = {}

  for log in logs:
    user_id, webpage = log.split(" ", maxsplit=1)

    if user_id in last_visited_page_by_user:
      last_visited_page = last_visited_page_by_user[user_id]
      transition = (last_visited_page, webpage)
      transitions[transition] = transitions.get(transition, 0) + 1

    last_visited_page_by_user[user_id] = webpage

  max_transitions = 0
  most_frequet_transition = None
  for transition in transitions:
    v = transitions[transition]
    if v > max_transitions:
      max_transitions = v
      most_frequet_transition = transition
  
  return {
    "max_transitions": max_transitions,
    "most_frequet_transition": most_frequet_transition,
  }



test_data = [
  "user1 /",
  "user1 /account",
  "user2 /service",
  "user2 /service/sub",
  "user3 /",
  "user3 /account",
]

if __name__ == "__main__":
  find_most_frequest_transition(test_data)
