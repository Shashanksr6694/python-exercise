import datetime
filename=datetime.datetime.now()
filename="resources/"+filename.strftime("%Y-%m-%d-%H-%M-%S-%f")
with open(str(filename),"w") as file:
    file.write("")
