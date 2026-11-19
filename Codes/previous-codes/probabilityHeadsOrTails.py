print("Lets to play heads or tails. Insert a number of spins to calculate the probability")
Total = int(input())
import random
coins = ["cara", "cruz"]
CCa = 0
CCr = 0
Pa = 0
Pr = 0
for i in range(1, Total):
  Calcu = random.choice(coins)
  if Calcu == coins(0):
    CCa += 1
  else:
    CCr += 1
Pa = (CCa / Total) * 100
Pr = (CCr / Total) * 100
print(f"Heads has come up {CCa}, which would be {Pa: .2f}% and tails has come up {CCr}, which would be {Pr: .2f}%.")
