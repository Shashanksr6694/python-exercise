file=open("resources/fruits.txt","r")
output=file.readlines()
file.close()
for i in output:
  print(i.rstrip("\n").__len__())
