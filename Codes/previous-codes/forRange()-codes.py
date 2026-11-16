# 1ST CODE TASK
Number = int(input())
for first in range(1, Number + 1):
  for second in range(1, Number + 1):
    result = first * second
    if result == Number:
            print(first, second)



# 2ND CODE TASK
first = int(input())
second = int(input())
# First even number bigger than 5
for i in range(first, second):
  if i % 2 == 0 and i > 5:
    print(f"First even number greater than 5: {i}")
    break
# First number divisible by 7
for l in range(first, second):
  if l % 7 == 0:
    print(f"First number divisible by 7: {l}")



# 3RD CODE TASKS
# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for i in range(30, 80 + 1):
    if i % 4 == 0:
        print(i, end=",")
print()  # line

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
count = 0
for i in range(15, 100):
  if i % 2 != 0:
    print(i, end=",")
    count += 1
    if count == 8:
      break
print()  # line

# Task 3: Counting backwards, divisible by 5 from 50
print("\nCounting backwards, divisible by 5 from 50:")
for i in range(50, 10 - 1, -1):
    if i % 5 == 0:
        print(i, end=",")

print()  # line

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
res = 1
for i in range(1, 30 + 1):
    if i % 3 == 0:
        res *= i
print(res)
