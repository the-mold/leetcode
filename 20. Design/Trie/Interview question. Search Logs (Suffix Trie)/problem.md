# Suppose you have many web documents and you want to serve search requests given a phrase. You need to return all matching documents that contain the exact search phrase.

# The sample sentences are:
# - the quick brown fox
# - the slow brown cow
# - to be or not to be that is the question
# - bar foo bar barfoo
# - ...millions of other web documents

# The search phrase and expected output are:
# - "brown" => ["the quick brown fox", "the slow brown cow"]
# - "slow brown" => ["the slow brown cow"]
# - "the cow" => []
# - "bar bar" => []
# - ...arbitratry user search phrase
