FINAL_POSITIONS = {
    1 : ['  ', True, [2,5,4]],
    2 : ['  ', True, [1,5,3]],
    3 : ['  ', True, [2,5,6]],
    4 : ['  ',True,[1,5,7]],
    5 : ['  ',True,[1,2,3,4,6,7,8,9]],
    6 : ['  ',True,[3,5,9]],
    7 : ['  ',True,[4,5,8]],
    8 : ['  ',True,[7,5,9]],
    9 : ['  ',True,[8,5,6]]
}

PLUCK_CAN_MOVE = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}

PLAYER1_NAME = 'Player-1'
PLAYER2_NAME = 'Player-2'

PLAYER_SYMBOLS = {
    PLAYER1_NAME : '🔴',
    PLAYER2_NAME : '🟡'
}

TrackFirstPlayerSymbol = []
TrackSecondPlayerSymbol = []

def Available_Positions():
    AvalPositions = []
    UnAvalPositions = []
    for i in range(1,10):
        if FINAL_POSITIONS[i][1]:
            AvalPositions.append(i)
        else:
            UnAvalPositions.append(i)
    return AvalPositions,UnAvalPositions

def Validate_Position(position):
    if position.isdigit():
        position = int(position)
        if 1 <= position <= 9:
            return position
        else:
            return False
    else:
        return False

def SelectWinner(position):
    if FINAL_POSITIONS[position][0] == PLAYER_SYMBOLS[PLAYER1_NAME]:
        return PLAYER1_NAME
    else:
        return PLAYER2_NAME

def isSumbolsMatched():
    if (FINAL_POSITIONS[1][0] == FINAL_POSITIONS[2][0] == FINAL_POSITIONS[3][0]) and ((FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(1)

    elif (FINAL_POSITIONS[4][0] == FINAL_POSITIONS[5][0] == FINAL_POSITIONS[6][0]) and ((FINAL_POSITIONS[4][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[4][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(4)

    elif (FINAL_POSITIONS[7][0] == FINAL_POSITIONS[8][0] == FINAL_POSITIONS[9][0]) and ((FINAL_POSITIONS[7][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[7][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(7)

    elif (FINAL_POSITIONS[1][0] == FINAL_POSITIONS[4][0] == FINAL_POSITIONS[7][0]) and ((FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(4)

    elif (FINAL_POSITIONS[2][0] == FINAL_POSITIONS[5][0] == FINAL_POSITIONS[8][0]) and ((FINAL_POSITIONS[2][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[2][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(2)

    elif (FINAL_POSITIONS[3][0] == FINAL_POSITIONS[6][0] == FINAL_POSITIONS[9][0]) and ((FINAL_POSITIONS[3][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[3][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(3)

    elif (FINAL_POSITIONS[1][0] == FINAL_POSITIONS[5][0] == FINAL_POSITIONS[9][0]) and ((FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[1][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(1)

    elif (FINAL_POSITIONS[3][0] == FINAL_POSITIONS[5][0] == FINAL_POSITIONS[7][0]) and ((FINAL_POSITIONS[3][0] == PLAYER_SYMBOLS[PLAYER1_NAME]) or (FINAL_POSITIONS[3][0] == PLAYER_SYMBOLS[PLAYER2_NAME])):
        return SelectWinner(3)

    return False

def Display_Data():
    print(f'{FINAL_POSITIONS[1][0]}───────{FINAL_POSITIONS[2][0]}───────{FINAL_POSITIONS[3][0]}\n'
          f'│ *       │      * │\n'
          f'│   *     │    *   │\n'
          f'│     *   │  *     │\n'
          f'{FINAL_POSITIONS[4][0]}───────{FINAL_POSITIONS[5][0]}───────{FINAL_POSITIONS[6][0]}\n'
          f'│      *  │  *     │\n'
          f'│    *    │    *   │\n'
          f'│  *      │      * │\n'
          f'{FINAL_POSITIONS[7][0]}───────{FINAL_POSITIONS[8][0]}───────{FINAL_POSITIONS[9][0]}')

def Display_symbols():
    print('********* Player Symbols **********')
    print('Player_Name\t-\tSymbol')
    print(f'{PLAYER1_NAME}\t-\t{PLAYER_SYMBOLS[PLAYER1_NAME]}')
    print(f'{PLAYER2_NAME}\t-\t{PLAYER_SYMBOLS[PLAYER2_NAME]}')

def SymbolMovingPositions(FilledPositions):
    for fposition in FilledPositions:
        ForPluckCanMove = []
        Con_Positions = FINAL_POSITIONS[fposition][2]
        for cPosition in Con_Positions:
            if FINAL_POSITIONS[cPosition][1]:
                ForPluckCanMove.append(cPosition)
        if ForPluckCanMove:
            PLUCK_CAN_MOVE[fposition] = ForPluckCanMove
            print(f'{fposition}th Pluck can moves to {ForPluckCanMove}')

def InsertSymbol(position, Player_name):

    if FINAL_POSITIONS[position][1]:
        FINAL_POSITIONS[position][0], FINAL_POSITIONS[position][1] = PLAYER_SYMBOLS[Player_name], False
    else:
        return False
    return True

def CommonCodeForPlayer(Player_name):
    while True:
        print(f'Hey {Player_name},place your symbol in a particular position? ')
        position = input()

        position = Validate_Position(position)
        if position:
            if InsertSymbol(position, Player_name):
                if Player_name == PLAYER1_NAME:
                    TrackFirstPlayerSymbol.append(position)
                else:
                    TrackSecondPlayerSymbol.append(position)
                break
            else:
                print('Position is Unavailable! already symbol placed, Choose another position.')
        else:
            print('Position is Invalid!')
    Display_Data()
def ShiftingPlucks(Playername, TrackPlayerPositions):
    TrackPlayerPositions.sort()
    print(f'Hey {Playername}, You Placed symbols at {TrackPlayerPositions}')
    SymbolMovingPositions(TrackPlayerPositions)
    while True:
        print(f'{Playername}! Enter which Pluck do want to move?')
        position = input()
        FromPosition = Validate_Position(position)
        if FromPosition not in TrackPlayerPositions:
            print(f'Invalid Position, Please enter from this only << {TrackPlayerPositions} >>')
        else:
            while True:
                print(f'{Playername}!Enter position where do you want to Shift?')
                position = input()
                ToPosition = Validate_Position(position)
                if ToPosition not in PLUCK_CAN_MOVE[FromPosition]:
                    print(f"You cann't move your Pluck {FromPosition} to {ToPosition} Position.")
                else:
                    FINAL_POSITIONS[FromPosition][0] = '  '
                    FINAL_POSITIONS[FromPosition][1] = True
                    TrackPlayerPositions.remove(FromPosition)
                    TrackPlayerPositions.append(ToPosition)
                    FINAL_POSITIONS[ToPosition][0] = PLAYER_SYMBOLS[Playername]
                    FINAL_POSITIONS[ToPosition][1] = False
                    break
        break
def Check_Winner():
    Winner_name = isSumbolsMatched()
    if Winner_name:
        print(f'Congratulations {Winner_name}! You Are The Winner')
        return True
    return False

def main():
    print('############## WELCOME TO SOS GAME ##############')
    print(f'1 ─────── 2 ─────── 3\n'
          f' │ *      │      * |\n'
          f' │   *    │    *   │\n'
          f' │     *  │  *     │\n'
          f'4 ─────── 5 ─────── 6\n'
          f' │      * │  *     │\n'
          f' │    *   │    *   │\n'
          f' │  *     │      * │\n'
          f'7 ─────── 8 ─────── 9')
    Display_Data()
    isPlacedAllSymbols = False
    Display_symbols()

    i = 1
    while i <= 3:
        CommonCodeForPlayer(PLAYER1_NAME)
        if Check_Winner() and i == 3: break

        CommonCodeForPlayer(PLAYER2_NAME)
        if Check_Winner() and i == 3: break

        i += 1
        if i == 4:
            isPlacedAllSymbols = True

    while isPlacedAllSymbols:
        ShiftingPlucks(PLAYER1_NAME,TrackFirstPlayerSymbol)
        Display_Data()
        if Check_Winner(): break

        ShiftingPlucks(PLAYER2_NAME,TrackSecondPlayerSymbol)
        Display_Data()
        if Check_Winner(): break

if __name__ == '__main__':
    main()