def currency_converter(rate,euros):
    return rate*euros

rate=float(input("Enter rate"))
euros=float(input("Enter euros"))
print(currency_converter(rate,euros))
