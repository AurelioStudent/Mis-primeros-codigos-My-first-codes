## Original code
import random
print("HOLA COMPAÑERO, QUIERES JUGAR AL PIEDRA PAPEL O TIJERAS?")
print("." * 25)
invent = ["piedra", "papel", "tijeras"]
reglas = {"piedra": "tijeras", "papel": "piedra", "tijeras": "papel"}
player = input().lower()
bot = random.choice(invent)
while True:
  if player == bot:
    print("Hemos empatado joder, otra?")
  elif reglas[player] == bot:
    print("Has ganado, pero quiero la revancha. Aceptas?")
  else:
    print("Has perdido, escribe salir y vete a llorar")
print("." * 25)
## English version
import random
print("HELLO FRIEND, DO YOU WANT TO PLAY ROCK, PAPER OR SCISSORS?")
print("." * 25)
invent = ["rock", "paper", "scissors"]
reglas = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
player = input().lower()
bot = random.choice(invent)
while True:
  if player == bot:
    print("We tied, damn it, another round?")
  elif reglas[player] == bot:
    print("You won, but I want a rematch. Do you accept?")
  else:
    print("You lost, type exit and go cry")
print("." * 25)
