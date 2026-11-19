print("Bienvenido a la Calculadora de interes compuesto y lineal. Primero escribe tu captital inicial, luego tu tasa de interés anual y por ultimo la cantidad de años que trabajará su dinero")
N = float(input("Capital inicial: "))
Y = float(input("Tasa de interés anual (ejemplo: 9 para 9%): "))
A = int(input("Cantidad de años: "))
ICC = N
ICS = N
CCC = N
CCS = N
duplicado = False
duplicado1 = False
for i in range(1, A + 1):
  CCC = (1 + Y / 100)
  CCS += ICS (Y / 100)
  print(f"En el año {i} has obtenido {CCC: .3f}€ con el interes compuesto y {CCS: .3f}€ con el interes simple")
  if CCC >= 2 * ICC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DUPLICADO EN EL AÑO {i}! CON EL INTERES COMPUESTO")
  if CCS >= 2 * ICS and duplicado1 == False:
    duplicado1 = True
    print(f"CAPITAL DUPLICADO EN EL AÑO {i}! CON EL INTERES LINEAL")
Result = CCC - CCS
print(f"LO MAS IMPORTANTE. La diferencia entre el interes compuesto frente al interes simple fue de {Result: .2f}€") 

# English version
print("Welcome to the compound and linear interest calculator. First enter your initial capital, then your annual interest rate and finally the number of years your money will work")
N = float(input("Initial capital: "))
Y = float(input("Annual interest rate (example: 9 for 9%): "))
A = int(input("Number of years: "))
ICC = N
ICS = N
CCC = N
CCS = N
duplicado = False
duplicado1 = False
for i in range(1, A + 1):
  CCC = (1 + Y / 100)
  CCS += ICS (Y / 100)
  print(f"In year {i} you have obtained {CCC: .3f}€ with compound interest and {CCS: .3f}€ with simple interest")
  if CCC >= 2 * ICC and duplicado == False:
    duplicado = True
    print(f"CAPITAL DOUBLED IN YEAR {i}! WITH COMPOUND INTEREST")
  if CCS >= 2 * ICS and duplicado1 == False:
    duplicado1 = True
    print(f"CAPITAL DOUBLED IN YEAR {i}! WITH LINEAR INTEREST")
Result = CCC - CCS
print(f"MOST IMPORTANT. The difference between compound interest and simple interest was {Result: .2f}€")
