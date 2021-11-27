### Greedy Algorithm
import time

coins = [2, 1, 0.25, 0.10, 0.01]
amount = 3.49

def give_the_change(coins, amount, change):
  # time.sleep(0.4)
  if amount == 0.0:
    return change
  for coin in coins:
    if coin <= amount:
      change.append(coin)
      new_amount = round(amount - coin, 2)
      change = give_the_change(coins, new_amount, change)
      return change
  return []

print(give_the_change(coins, amount, []))
