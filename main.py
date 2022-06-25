#chess stats engine

file = open('history.txt', 'r')
lines = file.readlines()
name = "yungsceezy"
games = []

for line in lines:
    
    #skip empty lines
    if line == "\n":
        continue
    
    #remove punctuation from line
    line = line.replace("\"", "")
    line = line.replace("[", "")
    line = line.replace("]", "")
    
    #split line into keywords and data
    words = line.split(' ')
    keyword = words[0]
    argument = words[1]
    argument = argument.replace("\n", "")
    
   #parse line for game results
    if keyword == "Result":
        #if draw
        if argument == "1/2-1/2":
            newdict["win"] = "draw"
        #if white wins
        elif argument == "1-0":
            if newdict["white"]:
                #if player is white
                newdict["win"] = True
            else:
                newdict["win"] = False
        #else black wins
        elif newdict["white"]:
                #if player is white
                newdict["win"] = False
        else:
                newdict["win"] = True
                
    #choose correct team based on player's name     
    if argument == name:
            if keyword == "White":
                newdict = {
                    "white": True
                }
            elif keyword == "Black":
                newdict = {
                    "white": False
                }
    if keyword == "1.":
        newdict["whitemoves"] = []
        newdict["blackmoves"] = []
        for i in range(len(words)):
                if i%3 == 1:
                    newdict["whitemoves"].append(words[i])
                elif i%3 == 2:
                    newdict["blackmoves"].append(words[i])
                    
        games.append(newdict)
     
whitegames = 0
whitewins = 0
blackgames = 0
blackwins = 0
whitedraws = 0
blackdraws = 0

# tally games for total win rates
for game in games:
    if game["white"]:
        whitegames += 1
        if game["win"] == "draw":
            whitedraws += 1
        elif game["win"]:
            whitewins += 1
        
    else:
        blackgames += 1
        if game["win"] == "draw":
            blackdraws += 1
        elif game["win"]:
            blackwins += 1

whiteWR = (whitewins + whitedraws/2)/whitegames
blackWR = (blackwins + blackdraws/2)/blackgames

# print win rates
# print("white games: " + str(whitegames) + "\n"
#      + "white wins: " + str(whitewins) + "\n"
#      + "white W/R: " + str(whiteWR))

# print("black games: " + str(blackgames) + "\n"
#      + "black wins: " + str(blackwins) + "\n"
#      + "black W/R: " + str(blackWR))

# print("white draws: " + str(whitedraws) + "\n"
#      + "black draws: " + str(blackdraws))

#opener calc
whiteopenings = {}
blackopenings = {}

for game in games:
    
    if game["white"]:
        move = game["whitemoves"][0]
        if move in whiteopenings:
            whiteopenings[move] = whiteopenings[move] + 1
        else:
            whiteopenings[move] = 1
    else:
        move = game["blackmoves"][0]
        if move in blackopenings:
            blackopenings[move] = blackopenings[move] + 1
        else:
            blackopenings[move] = 1
    
def filter_bymove(games_list, chosen_move, white, movenumber):
    if white:
        colour = "white"
    else:
        colour = "black"
    games = 0
    wins = 0
    draws = 0
    movenumber -= 1
    for game in games_list:
        if game[colour + "moves"][movenumber] == chosen_move:
            games+=1
            if game["win"] == "draw":
                draws+= 1
            elif game["win"]:
                wins+= 1

    return chosen_move + ", " + str(round(wins/games, 2)) + ", " + str(games) + " games"

print("white openings" + "\n")
for opening in whiteopenings:
    print(filter_bymove(games, opening, True, 1))
print("\n")

print("black openings" + "\n")
for opening in blackopenings:
    print(filter_bymove(games, opening, False, 1))
print("\n")

run = True
while(run):
    move = input("Choose opening\nType quit to exit\n")
    if(move.lower() == "quit"):
        run = False
    else:
        print(move + " chosen\n")

#def increment_win(variable):
# print("white openings: ", whiteopenings)
# print("black openings: ", blackopenings)

#for game in games:
#    print("white? " + str(game["white"]))
#    print("win? " + str(game["win"]))
#    print(game["whitemoves"])
#    print(game["blackmoves"])
#    print("\n")
