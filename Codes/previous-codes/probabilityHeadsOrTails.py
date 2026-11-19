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
print(f"El lado cara ha salido {CCa} veces que seria un {Pa: .2f}% de las veces y el lado cruz ha salido {CCr} veces que seria un {Pr: .2f}% de veces que se ha tirado la moneda.")
