year = 0
balance = int(input())
while balance < 700000:
    balance = balance + (balance * 7.1 / 100)
    year += 1
print(year)
