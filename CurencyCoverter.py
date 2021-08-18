with open("Currency.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

print(currencyDict)

amount = int(input("Enter amount:\n"))
print("Enter the name of currency you want to convert ?")
[print(item)for item in currencyDict.keys()]
currency = input("please enter oe of these values :")
print(f"{amount} INR is equal to {amount* float(currencyDict[currency])} {currency}")