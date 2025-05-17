due = 50
accepts_coins = [25,10,5]

while due>0:
    print("Amount Due:",due)
    inserted = int(input("Insert Coin: "))
    if inserted  in accepts_coins:
        due -= inserted

print("Change Owed:",abs(due))


