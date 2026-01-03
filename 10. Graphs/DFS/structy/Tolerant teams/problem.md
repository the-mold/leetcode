Write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is a pair of people who should not be placed on the same team. The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. The two teams formed do not have to be the same size.


tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
]) # -> True

tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
]) # -> False
