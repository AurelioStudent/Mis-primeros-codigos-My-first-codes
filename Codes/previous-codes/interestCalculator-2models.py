# original version:
# compound interest
print("Bienvenido a la Calculadora de interes compuesto. Primero escribe tu captital inicial, luego tu tasa de interés anual y por ultimo la cantidad de años que trabajará su dinero")
N = float(input("Capital inicial: "))
Y = float(input("Tasa de interés anual (ejemplo: 9 para 9%): "))
A = int(input("Cantidad de años: "))
IC = N
duplicado = False
for i in range(1, A + 1):
  N = (1 + Y / 100)
  print(f"En el año {i} has obtenido {N}")
  if N >= 2 IC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DUPLICADO EN EL AÑO {i}!")
# linear interest
print("Bienvenido a la Calculadora de interes lineal. Primero escribe tu captital inicial, luego tu tasa de interés anual y por ultimo la cantidad de años que trabajará su dinero")
N = float(input("Capital inicial: "))
Y = float(input("Tasa de interés anual (ejemplo: 9 para 9%): "))
A = int(input("Cantidad de años: "))
IC = N
duplicado = False
for i in range(1, A + 1):
  N += IC * (Y / 100)
  print(f"En el año {i} has obtenido {N}")
  if N >= 2 * IC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DUPLICADO EN EL AÑO {i}!")



# English version:
# compuond interest
print("Welcome to the compound interest calculator. First enter your initial capital, then your annual interest rate and finally the number of years your money will work")
N = float(input("Initial capital: "))
Y = float(input("Annual interest rate (example: 9 for 9%): "))
A = int(input("Number of years: "))
IC = N
duplicado = False
for i in range(1, A + 1):
  N = (1 + Y / 100)
  print(f"In year {i} you have obtained {N}")
  if N >= 2 * IC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DOUBLED IN YEAR {i}!")
# linear interest
    print("Welcome to the linear interest calculator. First enter your initial capital, then your annual interest rate and finally the number of years your money will work")
N = float(input("Initial capital: "))
Y = float(input("Annual interest rate (example: 9 for 9%): "))
A = int(input("Number of years: "))
IC = N
duplicado = False
for i in range(1, A + 1):
  N += IC * (Y / 100)
  print(f"In year {i} you have obtained {N}")
  if N >= 2 * IC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DOUBLED IN YEAR {i}!")
