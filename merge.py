import datetime
filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")

file=open("resources/"+filename,"a")

files=["resources/content1.txt","resources/content2.txt","resources/content3.txt"]

for f in files:
  tmp=open(f,"r")
  file.write(tmp.read())
  tmp.close()

file.close()
