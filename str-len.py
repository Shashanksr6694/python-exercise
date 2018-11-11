def length(str):
    if type(str) == int or type(str) == float:
        print("Sorry integers/float don't have length")
    else:
        return len(str)

str=input("Enter a string")
print(length(10.0))
