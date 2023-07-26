import os
import time


class TikTakToe:
    def __init__(self, player1_name="player1", player2_name="player2"):
        self.X_VALUE = "✘"
        self.O_VALUE = "☻"
        self.current_value = self.X_VALUE
        self.sample_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.user_entery = []
        self.player1 = player1_name.title()
        self.player2 = player2_name.title()
        self.__player1_score = 0
        self.__player2_score = 0

    def __display(self):
        print(
            f"{self.player1} score: {self.__player1_score} {self.player2} score: {self.__player2_score}\nBellow is given box you can choose anyone from 1 2 3..9: ")
        print(f" _____ _____ _____ ")
        for valu in self.board:
            print(end="| ")
            for num in valu:
                print(f" {num} ", end=" | ")
            print(f"\n|_____|_____|_____|")

    def __winner(self):
        status = False
        for valu in self.board:
            if (valu[0] != " " and valu[1] != " " and valu[2] != " ") and (valu[0] == valu[1] == valu[2]):
                status = True
        for i in range(0, 3):
            if (self.board[0][i] != " " and self.board[1][i] != " " and self.board[2][i] != " ") and (
                    self.board[0][i] == self.board[1][i] == self.board[2][i]):
                status = True
        if ((self.board[0][0] != " " and self.board[1][1] != " " and self.board[2][2] != " ") and (
                self.board[0][0] == self.board[1][1] == self.board[2][2])) or (
                (self.board[0][2] != " " and self.board[1][1] != " " and self.board[2][0] != " ") and (
                self.board[0][2] == self.board[1][1] == self.board[2][0])):
            status = True
        return status

    def __change_current_value(self):
        if self.current_value == self.X_VALUE:
            self.current_value = self.O_VALUE
        else:
            self.current_value = self.X_VALUE

    def __chage_values_board(self, user_input):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.sample_board[i][j] == user_input:
                    self.board[i][j] = self.current_value
                    self.__change_current_value()

    def __user_input(self):
        self.clear()
        self.__display()
        if self.current_value == self.X_VALUE:
            user_input = input(f"{self.player1} Your Turn: ")
        else:
            user_input = input(f"{self.player2} Your Turn: ")
        if int(user_input) > 9 or int(user_input) < 1:
            print("Wrong Input")
            time.sleep(2)
        else:
            if user_input not in self.user_entery:
                self.user_entery.append(user_input)
                self.__chage_values_board(user_input)
            else:
                print("Already exit try another cell ????")
                time.sleep(2)

    def __clear_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                self.board[i][j] = " "
        self.user_entery = []
        self.clear()

    def result(self):
        for i in range(0,10):
            for j in range(0, i):
                print(".", sep=" ", end="")
                time.sleep(0.1)
            self.clear()

        time.sleep(1)
        if self.__player1_score > self.__player2_score:
            print(f"{self.player1} 😎 congratulation you won \( ﾟヮﾟ)/🏆🏆🏆🏆🏆!!")
        elif self.__player2_score > self.__player1_score:
            print(f"{self.player2} 😎 congratulation you won \( ﾟヮﾟ)/🏆🏆🏆🏆🏆!!!!!")
        else:
            print(f"{self.player1} 🆚 {self.player2} match draw😑.....")
        time.sleep(2)

    def play(self):
        for i in range(0, 9):
            self.clear()
            self.__user_input()
            if self.__winner():
                self.clear()
                if self.current_value == self.X_VALUE:
                    self.__player2_score += 1
                    self.__display()
                    print(f"Hurray!!! {self.player2} Won.")
                else:
                    self.__player1_score += 1
                    self.__display()
                    print(f"Hurray!!! {self.player1} Won.")
                break
            if i == 8:
                print(f"{self.player1} Vs {self.player2} Draw. Better Luck next time")
        time.sleep(2)
        self.__clear_board()

    def clear(self):
        if os.name == "nt":
            _ = os.system('cls')
        else:
            _ = os.system('clear')
