# Jared Jackson
# 10/09/19
# we will be learning about While Loops

i = 0

numbers = []

while i < 6:
    print(f"Atb the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
