import random
from art import logo, vs
from game_data import data

score = 0
is_game_over = False
contestant1 = random.choice(data)
contestant2 = random.choice(data)

if contestant1 == contestant2:
  contestant2 = random.choice(data)

def comparison(a, b):
  return a > b

print(logo)

while not is_game_over:
  a_follow_count = contestant1['follower_count']
  b_follow_count = contestant2['follower_count']
  print(f"Compare A: {contestant1['name']}, a {contestant1['description']}, from {contestant1['country']}.")

  print(vs)

  print(f"\nCompare B: {contestant2['name']}, a {contestant2['description']}, from {contestant2['country']}.")

  player_guess = input("\nWho has the most followers, A or B?\n").lower()

  if player_guess == "a" and comparison(a_follow_count, b_follow_count):
    print("Correct!")
    score += 1
    print(f"Score: {score}")
    contestant2 = random.choice(data)
  elif player_guess == "b" and comparison(a_follow_count, b_follow_count) == False:
    print("Correct!")
    score += 1
    print(f"Score: {score}")
    contestant1 = contestant2
    contestant2 = random.choice(data)
  else:
    print("Incorrect!")
    print(f"Score: {score}")
    is_game_over = True
  