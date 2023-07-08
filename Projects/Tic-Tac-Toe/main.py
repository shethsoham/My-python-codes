
def sum (a,b, c):
    return a + b + c 

def printboard(xState, zState):
    
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    #pass #when you have not written any logic insde a function 
def checkWin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8,],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:

        if (sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print(printboard(xState,zState))
            print("X Won the match ")
            return 1
        if (sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            print("O Won the match ")
            return 0
    return -1 
if __name__ == "__main__":

# This means when ever you are running your python program then
# i.e. main file then it will only import the main file
# It will not execute the program it will just import the functions
#Even if you don't use it it is fine 
    xState = [0,0,0,0,0,0,0,0,0]# 9 blocks
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and  0 for O
    print("Welcome to Play Tic Tac Toe")
    while(True):
        printboard(xState, zState)
        if (turn == 1 ):
            print("X's Chance")
            value = int(input("Please enter a value : "))
            xState[value] = 1
        else :
            print("O's Chance")
            value = int(input("Please enter a value : "))
            zState[value] = 1
        cWin = checkWin(xState,zState )
        if(cWin != -1):
            print("Match Over")
            break
        
        turn = 1- turn 

 