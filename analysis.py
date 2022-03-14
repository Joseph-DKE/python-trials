print("Welcome to the three match analysis system \n")
print("For more explanation, kindly visit https://t.me/rmsbywsb on telegram. \n \n")

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
while team < teams:
    while outcome < outcomes:
        teamnames[team][outcome] = input("Enter name for team or draw if draw: \n")
        odds[team][outcome] = float(input("Enter corresponding odd for team " + teamnames[team][outcome] + "\n"))
#        odds[team][outcome] = float(temporaryinput)
        outcome += 1
    outcome = 0
    team += 1

#space to store fixed amount per bet
price = float(input("Enter price: \n"))

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

#checking number of profitable outcomes
#counter = 0
#total_profitable_outcomes = 0
total_price = price * bets
#while counter < 27:
#    if finaloutcome[counter] > (total_price):
#        total_profitable_outcomes += 1
#    counter += 1

#checking probability of success
#finalprobability = total_profitable_outcomes / bets
#probabilitypercent = finalprobability * 100
#negprobper = 100 - probabilitypercent

#printing out results
#print("You have a " + str(probabilitypercent) + " percent of making a profit and a " + str(negprobper) + " percent of making a loss. \n")
#print("Highly Impossible Outcomes: \n")

#finding bets below average odds
averageoutcome = 0.00
ccount = 0
while ccount < bets:
    averageoutcome += finaloutcome[ccount]
    ccount += 1
averageoutcome = averageoutcome / bets

#counter = 0
#totcount = 0
#while counter < bets:
#    if finaloutcome[counter] > (total_price):
#        print(str(finaloutcome[counter]) + " [||] " + str(odds_sequence[counter]))
#        totcount += 1
#    counter += 1
#print("Total number = " + str(totcount))


#line break
#print("\n")

#print("Highly Possible Outcomes:")
counter = 0
totpossiblecount = 0
averagepossible = 0.00
possibleoutcomestring = "--------------------------\n"
while counter < bets:
    if finaloutcome[counter] < (total_price):
#        possibleoutcomestring += str(finaloutcome[counter]) + " \n " + str(odds_sequence[counter]) + "\n--------------------------\n"
        averagepossible += finaloutcome[counter]
        totpossiblecount += 1
    counter += 1
averagepossible = averagepossible / totpossiblecount
print("Total possible number = " + str(totpossiblecount))
#print(possibleoutcomestring)

#print("--------------------------\n")

#print("Outcomes Below Average Odds:")
counter = 0
totaveragecount = 0
averageoutcomestring = "--------------------------\n"
while counter < bets:
    if finaloutcome[counter] < (averageoutcome):
#        averageoutcomestring += str(finaloutcome[counter]) + "\n" + str(odds_sequence[counter]) + "\n--------------------------\n"
        totaveragecount += 1
    counter += 1
#averageaverage = averageaverage / totaveragecount
print("Total average number = " + str(totaveragecount))
#print(averageoutcomestring)

#print("--------------------------\n")

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

lespocheck = 0
lespo = lessertotpossiblecount
while lespo < lowestoutcome:
    lespo += 1
    lespocheck += 1
lespocheck -= 1

lespochecksave = lespocheck

tempoutcome.sort()

counter = 0
while counter < bets:
    if tempoutcome[counter] > (highestoutcome):
        break
    counter += 1

lastlist = ""
nextcounter = 0
while lespocheck > 0:
    while nextcounter < bets:
        if finaloutcome[nextcounter] == tempoutcome[counter]:
            lastlist += str(finaloutcome[nextcounter]) + " \n " + str(odds_sequence[nextcounter]) + " \n " + str(names_sequence[nextcounter]) + "\n--------------------------\n"
            counter += 1
            break
        nextcounter += 1
    nextcounter = 0
    lespocheck -= 1    

#if (totpossiblecount - totaveragecount) > 4:
print("GOOD TO GO!")
print("Bet on these odds and outcomes. \n")
print("Final Total possible number = " + str(lessertotpossiblecount + lespochecksave))
print(lesserpossibleoutcomestring + lastlist)
#elif (totpossiblecount - totaveragecount) > 2:
#    print("Great Circumstance!")
#elif (totpossiblecount - totaveragecount) < -2:
#    print("You really shouldn't use this strategy to bet.")
#elif (totpossiblecount - totaveragecount) < 0:
#    print("You are advised not to use this strategy to make a bet.")
#else:
#    print("DO NOT BET!")

#print("Bet on these odds and outcomes. \n")
#print(possibleoutcomestring)
#print("Total bets = " + str(totpossiblecount))
#print("Total price = " + str(price * totpossiblecount))

#print("--------------------------")
#print("--------------------------\n")
#print("Bet on these odds and outcomes. \n")
#print("Total possible number(Reduced) = " + str(lessertotpossiblecount))
#print(lesserpossibleoutcomestring)

#print("--------------------------")
#print("--------------------------\n")
#print("Bet on these odds and outcomes. \n")
#print("Final Total possible number = " + str(lessertotpossiblecount + lespochecksave))
#print(lesserpossibleoutcomestring + lastlist)
