import random
class Tic_tac_toe():

    def __init__(self):
        self.gameboard = ["", "", "", "", "", "","", "", ""]
        self.end_state = False

    def updateBoard(self, position, player):
        self.gameboard[position] = player

    def checkWinCondition(self):
        if self.gameboard[0] != "" and self.gameboard[0] == self.gameboard[1] and self.gameboard[1] == self.gameboard[2]:
            return True, self.gameboard[0]
        if self.gameboard[0] != "" and self.gameboard[0] == self.gameboard[4] and self.gameboard[4] == self.gameboard[8]:
            return True, self.gameboard[0]
        if self.gameboard[0] != "" and self.gameboard[0] == self.gameboard[3] and self.gameboard[3] == self.gameboard[6]:
            return True, self.gameboard[0]
        if self.gameboard[1] != "" and self.gameboard[1] == self.gameboard[4] and self.gameboard[4] == self.gameboard[7]:
            return True, self.gameboard[1]
        if self.gameboard[2] != "" and self.gameboard[2] == self.gameboard[5] and self.gameboard[5] == self.gameboard[8]:
            return True, self.gameboard[2]
        if self.gameboard[2] != "" and self.gameboard[2] == self.gameboard[4] and self.gameboard[4] == self.gameboard[6]:
            return True, self.gameboard[2]
        if self.gameboard[3] != "" and self.gameboard[3] == self.gameboard[4] and self.gameboard[4] == self.gameboard[5]:
            return True, self.gameboard[3]
        if self.gameboard[6] != "" and self.gameboard[6] == self.gameboard[7] and self.gameboard[7] == self.gameboard[8]:
            return True, self.gameboard[6]
        return False, ""

    def checkStalemate(self):
        for value in self.gameboard:
            if value == "":
                return False
        return True

    def makeComputerMove(self):
        select = random.randint(0,8)
        while self.gameboard[select] != "":
            if select == 8:
                select = 0
            else:
                select += 1
        self.updateBoard(select, "O")