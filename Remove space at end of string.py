stringss = "hello "
if stringss[-1] == ' ':
    lenSt = len(stringss)
    stringss = stringss[0:lenSt-1]
if stringss[-1] == ' ':
    print("yay")
print(stringss + stringss)