#space to store odds
teams = 3
outcomes = 3
odds = [[0 for x in range(outcomes)] for y in range(teams)]
teamnames = [[0 for x in range(outcomes)] for y in range(teams)]

#total chances
bets = 27 #* 3

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
stringList = "Man 1.2 DRAW 4.0 Arsenal 5.1 Juve 2.1 DRAW 1.2 Chelsea 3.3 Liverpool 4.2 DRAW 5.5 Tottenham 1.8"
integerTempList = ''
integerList = []
namesList = []
iac = 0
while iac < 9:
    integerList.append(0.00)
    namesList.append('')
    iac += 1

namesTempList = ''

position = 0
while position < len(stringList):
    if stringList[position].isnumeric() or stringList[position] == '.':
        integerTempList += stringList[position]
    elif stringList[position] == ' ' or stringList[position] == '\n':
        integerTempList += '~'
    position += 1

integerTempList += '~~'

counttter = 0
integerListtt = ''
position = 1
while counttter < 9:
    if integerTempList[position].isnumeric() or integerTempList[position] == '.':
        integerListtt += integerTempList[position]
    else:
        integerList[counttter] = float(integerListtt)
        integerListtt = ''
        counttter += 1
        position += 1
    position += 1

#list of names
position = 0
while position < len(stringList):
    if not stringList[position].isnumeric() and stringList[position] != '.':
        namesTempList += stringList[position]
    position += 1

namesTempList += '  '
counttter = 0
namesListtt = ''
position = 0
while counttter < 9:
    if namesTempList[position] != ' ':
        namesListtt += namesTempList[position]
    else:
        namesList[counttter] = namesListtt
        namesListtt = ''
        counttter += 1
        position += 1
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

#space to store fixed amount per bet
price = 1.00

#setting counter
counter = 0

#for saving each sequence
odds_sequence = []
names_sequence = []
tempcount = 0
while tempcount < bets:
    odds_sequence.append(0)
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
            totalodds[count] = odds[0][i] * odds[1][j] * odds[2][k] #* odds[3][l]
            odds_sequence[count] = "(" + str(odds[0][i]) + ") | (" + str(odds[1][j]) + ") | (" + str(odds[2][k]) + ")" #| (" + str(odds[3][l]) + ")"
            names_sequence[count] = str(teamnames[0][i]) + " | " + str(teamnames[1][j]) + " | " + str(teamnames[2][k]) #+ " | " + str(teamnames[3][l])
            count += 1
            k += 1
        k = 0
        j += 1
    j = 0
    i += 1

#calculating potential profits
while counter < bets:
    finaloutcome[counter] = price * totalodds[counter]
    tempoutcome[counter] = finaloutcome[counter]
    counter += 1

total_price = price * bets

#finding bets below average odds
averageoutcome = 0.00
ccount = 0
while ccount < bets:
    averageoutcome += finaloutcome[ccount]
    ccount += 1
averageoutcome = averageoutcome / bets

#print("Highly Possible Outcomes:")
counter = 0
totpossiblecount = 0
averagepossible = 0.00
possibleoutcomestring = "--------------------------\n"
while counter < bets:
    if finaloutcome[counter] < total_price:
        averagepossible += finaloutcome[counter]
        totpossiblecount += 1
    counter += 1

averagepossible /= totpossiblecount

counter = 0
totaveragecount = 0
averageoutcomestring = "--------------------------\n"
while counter < bets:
    if finaloutcome[counter] < (averageoutcome):
        totaveragecount += 1
    counter += 1

counter = 0
lessertotpossiblecount = 0
lesseraveragepossible = 0.00
highestoutcome = 0.00
lowestoutcome = 50000.00
lesserpossibleoutcomestring = "--------------------------\n"
while counter < bets:
    if finaloutcome[counter] < (averagepossible):
        lesserpossibleoutcomestring += str(finaloutcome[counter]) + " \n " + str(odds_sequence[counter]) + " \n " + str(names_sequence[counter]) + "\n--------------------------\n"
        lessertotpossiblecount += 1
        if highestoutcome < finaloutcome[counter]:
            highestoutcome = finaloutcome[counter]
        if lowestoutcome > finaloutcome[counter]:
            lowestoutcome = finaloutcome[counter]
    counter += 1

tempoutcome.sort()

counter = 0
while counter < bets:
    if tempoutcome[counter] > (highestoutcome):
        break
    counter += 1  

leaka = lessertotpossiblecount
if (totpossiblecount - totaveragecount) > 4:
    print("GOOD TO GO!")
    print("Bet on these odds and outcomes. \n")
    print("\nTotal bets = " + str(leaka) + "\n\n")
    print(lesserpossibleoutcomestring)
else:
    print("DO NOT BET!")
