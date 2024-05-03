import argparse

def generate_matches(numOfMatches, numOfPlayers):
    num_players = numOfPlayers
    listOfMatches = []
    rowIndex = 0
    # Adjust the number of players as needed and times to play
    players = [f'Player {i}' for i in range(1, numOfPlayers+1)]
    
    #create cross matrix of number of matches to be played
    cross_matrix = [[numOfMatches for x in range(num_players)] for y in range(num_players)]

    
    #reset the values to play against itself
    for i in range(0, num_players):
        cross_matrix[i][i] = 0
    
    #check each row for players to play against
    for players_in_row in cross_matrix:
        # row index marks the actual player which row is starting with
        localMatches = createMatchesFor4PlayersInRow(rowIndex, players_in_row)
        for match in localMatches:
            listOfMatches.append(match)
        cross_matrix = reduceNumberOfTimesToPlay(localMatches, cross_matrix)
        rowIndex+=1
    
    return listOfMatches

def createMatchesFor4PlayersInRow(actPlayerIdx, players_in_row):
    listOfMatches = []
    
    while(max(players_in_row)>0): 
        singleMatch = []
        
        # Enumerate the list to get indices and values, then sort by values
        sorted_indices = sorted(enumerate(players_in_row), key=lambda x: x[1], reverse=True)

        # Take the indices of the first 3 highest values
        top_3_indices = [index for index, _ in sorted_indices[:3]]
        
        singleMatch.append(actPlayerIdx)
        
        # check each player if they still need to play
        for playerIdx in top_3_indices:
            if (players_in_row[playerIdx]>0):
                # add to single match         
                singleMatch.append(playerIdx)
                #remove the times to play
                players_in_row[playerIdx]-=1
                
        listOfMatches.append(singleMatch)
                     
    return listOfMatches

def reduceNumberOfTimesToPlay(listOfMatches, cross_matrix):
    # check for each match
    for match in listOfMatches:
        # the players if they still have to play and decrement
        for playerIdx in match:
            if(cross_matrix[playerIdx][playerIdx]>0):
                cross_matrix[playerIdx][playerIdx] -= 1
            if(cross_matrix[playerIdx][playerIdx]>0):
                cross_matrix[playerIdx][playerIdx] -= 1
    return cross_matrix

def saveMatchesToCsvFile(matches, fname):
    strOfMatches = ""
    # create csv out of the matches, including Player Number
    for i, match in enumerate(matches):
        strOfMatches += 'Match '+(str(i+1)) 
        for playerNbr in match:
            strOfMatches += ';Player '+str(playerNbr)
        strOfMatches += '\n'
    
    # save as CSV file
    f = open(fname, "w+")
    f.write(strOfMatches)
    f.close()

def parseArgumentsForMarioKartLeague():
    parser = argparse.ArgumentParser(description='Generate Matchlist for Mario Kart')
    parser.add_argument('--player', help='How many Player', default=10)
    parser.add_argument('--times', help='How many times each Player needs to play', default=2)
    parser.add_argument('--fname', help='Name of CSV File', default='mariokart')
    args = parser.parse_args()
    print(str(args.player)+' Players, play '+str(args.times)+' matches, saving to file '+args.fname+'.csv')
    
    return int(args.times), int(args.player), str(args.fname+'.csv')

def main():
    numOfMatches, numOfPlayers, strFname = parseArgumentsForMarioKartLeague()
    
    # generate the matches list
    matches = generate_matches(numOfMatches, numOfPlayers)
    
    # convert to CSV list
    saveMatchesToCsvFile(matches, strFname)

if __name__ == "__main__":
    main()