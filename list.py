HELLO = ["hello", "hi"]
GOODBYE = ["goodbye", "bye"]

POLITENESS = [HELLO, GOODBYE]

FRUITS = ["apples", "bananas"]
MEAT = ["pork", "chicken"]

FOODS = [FRUITS, MEAT]

random_Words = ["shoe", "bicycle", "school"]


#Here is the triple nested list.
VOCABULARY = [POLITENESS, FOODS, random_Words, "house"]

knowWord = False
userInput = input("say whatever ")


def findWord(word,l):
    words = []
    lists = []
    for entry in l:
        if isinstance(entry,list):
            lists.append(entry)
        else:
            words.append(entry)


    for w in words:
        if w == word:
            return True
    
    for ls in lists:
        if findWord(word,ls) == True:
            return True

    return False



if findWord(userInput,VOCABULARY) == True:
    print("YES")
else:
    print("I don't know that word")
