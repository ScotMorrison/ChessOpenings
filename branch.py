import re
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

        v = re.compile(r"(\bO(\-O)*\b|([N,Q,R,K,B]?([a-h]?|[0-8]?)([x]?)([a-h][0-8])([\+\#]?)))")
        mv_list = v.findall(line)     

        for i in range(len(mv_list)):
            if i % 2 == 0:
                newdict["whitemoves"].append(mv_list[i][0])
            else:
                newdict["blackmoves"].append(mv_list[i][0])         
        games.append(newdict)

def validMove(move):
    # regex to verify valid algebraic notation moves
    # returns true for valid moves, false otherwise
    v = re.compile(r'^([n,q,r,k,b]?)([a-h]?|[0-8]?)([x]?)([a-h][0-8])([\+\#]?)$')
    if v.match(move) is not None:
        return True
    if move == ("o-o" or "o-o-o"):
        return True
    else: 
        return False

def filterByColour(games_list, white):
    glist = []
    for game in games_list:
        if(white == game["white"]):
            glist.append(game)
    return glist

def filterBySeries(games_list, move_list, chosen_move, white, iteration):
    #base case
    if white:
            colour = "whitemoves"
    else:
            colour = "blackmoves"
    if(not move_list):
        games = 0
        wins = 0
        for game in games_list:
            if game[colour][iteration].lower() == chosen_move.lower():
                games+=1
                if game["win"] != "draw" and game["win"]:
                    wins+=1
        if(games):
            return(chosen_move, games, round(wins/games,2), m_list)
        else:
            return(chosen_move, 0)
    #recursive call
    else:
        glist = []
        for game in games_list:
            if(game[colour][iteration].lower() == move_list[0].lower()):
                glist.append(game)
        return filterBySeries(glist, move_list[1:], chosen_move, white, iteration+1)

def displayMoves(games_list, move_list, white, iteration):

    if white:
        colour = "whitemoves"
    else:
        colour = "blackmoves"

    #base case
    if not move_list:
        return_list = []
        for game in games_list:
            if(white == game["white"]):
                if game[colour][iteration] not in return_list:
                    return_list.append(game[colour][iteration])
        return return_list

    #recursive call
    else:
        filtered_game_list = []
        for game in games_list:
            if game[colour][iteration] == move_list[0]:
                filtered_game_list.append(game)
        return displayMoves(filtered_game_list, move_list[1:], white, iteration+1)

#main program loop

print("choose side: w for white, b for black")

run = True

while(run):
    side = input().lower()
    if side == "w":
        side = True
        run = False
    elif side == "b":
        side = False
        run = False
    else:
        print("please try again: w for white, b for black")

run = True
m_list = []

print("Choose opening\nType quit to exit\n")
print(displayMoves(games, m_list, side, 0))

while(run):
    move = input().lower()
    if(not move):
        continue
    if(move == "quit"):
        run = False
    if(move == "back"):
        m_list = m_list[:-1]
        print("\nCurrent line: " + str(m_list))
        print("Variations available\n" + str(displayMoves(games, m_list, side, 0)))
    else:
        if validMove(move):
            v = re.compile(r'[n, k, q, r]|[b][a-h]')
            if v.match(move) is not None:
                 move = move[0].upper() + move[1:]
            filtered_list = filterByColour(games, side)
            g = filterBySeries(filtered_list, m_list, move, side, 0)
            if(g[1]):
                m_list.append(g[0])
                print("\n\nMove: " + str(g[0]) + "\nGames: " + str(g[1]) + "\nWin Rate: " + str(g[2]) + "\nCurrent Line: " + str(g[3]))
            else:
                print(g[0] + " has not been played in this variation\n")
            print("\nChoose Variation:\n")
            print(displayMoves(games, m_list, side, 0))
            print("\n")
            continue
    
    
