#space to store odds
teams = 4
outcomes = 3
odds = [[0 for x in range(outcomes)] for y in range(teams)]
teamnames = [[0 for x in range(outcomes)] for y in range(teams)]

#total chances
bets = 27 * 3

#space to store total odds
totalodds = []

#space to store each outcome
finaloutcome = []
tempoutcome = []

#geting 27 spaces in finaloutcome and totalodds
tempcounter = 0
while tempcounter < bets:
    totalodds.append(0.00)
    tempoutcome.append(0.00)
    finaloutcome.append(0.00)
    tempcounter += 1

#getting odds
team = 0
outcome = 0
stringList = str(input("Type Here: "))
integerTempList = ''
integerList = []
namesList = []
iac = 0
while iac < 12:
    integerList.append(0.00)
    namesList.append('')
    iac += 1

namesTempList = ''

position = 0
while position < len(stringList):
    if stringList[position].isnumeric() or stringList[position] == '.':
        integerTempList += stringList[position]
    elif stringList[position] == " ":
        integerTempList += '~'
    position += 1

integerTempList += '~~'

counttter = 0
integerListtt = ''
position = 2
if integerTempList[position] == '.':
    position -= 1
while counttter < 12:
    if integerTempList[position].isnumeric() or integerTempList[position] == '.':
        integerListtt += integerTempList[position]
        position += 1
    else:
        integerList[counttter] = float(integerListtt)
        integerListtt = ''
        counttter += 1
        if counttter == 12:
            break
        while not integerTempList[position].isnumeric():
            position += 1

#list of names
position = 0
while position < len(stringList):
    if stringList[position].isalpha() or stringList[position] == ' ':
        namesTempList += stringList[position]
    elif stringList[position] == '.':
        namesTempList += "~"
    position += 1

namesTempList += '~~'

counttter = 0
namesListtt = ''
position = 0
while counttter < 12:
    if namesTempList[position] != '~':
        namesListtt += namesTempList[position]
    else:
        namesList[counttter] = namesListtt
        namesListtt = ''
        counttter += 1
    position += 1

position = 0
while team < teams:
    while outcome < outcomes:
        teamnames[team][outcome] = namesList[position]
        odds[team][outcome] = integerList[position]
        position += 1
        outcome += 1
    outcome = 0
    team += 1


#for saving each sequence
odds_sequence = []
names_sequence = []
tempcount = 0
while tempcount < bets:
    odds_sequence.append("")
    names_sequence.append("")
    tempcount += 1

#calculating each total odd
i = 0
j = 0
k = 0
l = 0
count = 0
while i < outcomes:
    while j < outcomes:
        while k < outcomes:
            while l < outcomes:
                totalodds[count] = float(odds[0][i]) * float(odds[1][j]) * float(odds[2][k]) * odds[3][l]
                odds_sequence[count] = "(" + str(odds[0][i]) + ") | (" + str(odds[1][j]) + ") | (" + str(odds[2][k]) + ") | (" + str(odds[3][l]) + ")" #| (" + str(odds[3][l]) + ")"
                names_sequence[count] = str(teamnames[0][i]) + " | " + str(teamnames[1][j]) + " | " + str(teamnames[2][k]) + " | " + str(teamnames[3][l]) #+ " | " + str(teamnames[3][l])
                count += 1
                l += 1
            l = 0
            k += 1
        k = 0
        j += 1
    j = 0
    i += 1


#calculating potential profits
counter = 0
while counter < bets:
    finaloutcome[counter] =  totalodds[counter]
    tempoutcome[counter] = finaloutcome[counter]
    counter += 1


counter = 0
highestoutcome = 0.00
lowestoutcome = 50000.00
while counter < bets:
    if highestoutcome < finaloutcome[counter]:
        highestoutcome = finaloutcome[counter]
    if lowestoutcome > finaloutcome[counter]:
        lowestoutcome = finaloutcome[counter]
    counter += 1

tempoutcome.sort()

cappoint = int(lowestoutcome)
cappointP = (cappoint / bets) * 100
if cappointP <= 50:
    results = "RISKY BET! \n"
else:
    results = "GOOD TO GO!\n"
results += "Bet the same amount on each of these outcomes.\n"
results += "Total bets = " + str(cappoint) + "\n"
results += "Chance of success: " + str(cappointP) + "\n\n"
counter = 0
counter2 = 0
while counter < bets:
    while counter2 < bets:
        if tempoutcome[counter] == finaloutcome[counter2]:
            results += "Total Odds: " + str(finaloutcome[counter2]) + "\nOdds: " + str(odds_sequence[counter2]) + "\nTeams: " + str(names_sequence[counter2]) + "\n\n\n"
            finaloutcome.pop(counter2)
            odds_sequence.pop(counter2)
            names_sequence.pop(counter2)
            break
        else:
            counter2 += 1
    counter2 = 0
    counter += 1
print(results)
