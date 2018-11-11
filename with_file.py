with open("resources/example_new.txt","a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nNew line")

print(content)
