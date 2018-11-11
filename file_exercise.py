temperatures=[10,-20,-289,100]
def c_to_f(c):
    f=c*9/5+32
    return f
file=open("resources/temperature.txt","w")
for t in temperatures:
    temp=c_to_f(t)
    if temp> -273.15:
      print(temp)
      file.write(str(temp)+"\n")
file.close()
