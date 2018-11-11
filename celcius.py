def cel_to_faran(cel):
    return (float(cel)*9/5)+32

cel=input("Enter temperature in celcius")

temperatures=[10,-20,-289,100]
for temperature in temperatures:
    if float(temperature) < -273.15:
        print("Not possible")
    else:
        print(cel_to_faran(temperature))
