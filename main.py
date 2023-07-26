# X_VALUE = "✘"
# O_VALUE = "☻"
import time

X_VALUE = "✘"
O_VALUE = "☻"
import os


class TikTakToe:
    def __init__(self, player1_name="player1", player2_name="player2"):
        self.current_value = X_VALUE
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.user_entery = []
        self.player1 = player1_name.title()
        self.player2 = player2_name.title()

    def display(self):
        print(
            f"{self.player1} value: X {self.player2} value: O\nBellow is given box you can choose anyone from 1 2 3..9: ")
        print(f" _____ _____ _____ ")
        for valu in self.board:
            print(end="| ")
            for num in valu:
                print(f" {num} ", end=" | ")
            print(f"\n|_____|_____|_____|")

    def winner(self):
        status = False
        for valu in self.board:
            if valu[0] == valu[1] == valu[2]:
                status = True
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                status = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == \
                self.board[2][0]:
            status = True
        return status

    def change_current_value(self):
        if self.current_value == X_VALUE:
            self.current_value = O_VALUE
        else:
            self.current_value = X_VALUE

    def chage_values_board(self, user_input):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == user_input:
                    self.board[i][j] = self.current_value
                    self.change_current_value()

    def user_input(self):
        self.display()
        if self.current_value == X_VALUE:
            user_input = input(f"{self.player1} Your Turn: ")
        else:
            user_input = input(f"{self.player2} Your Turn: ")
        if int(user_input) > 9 or int(user_input) < 1:
            print("Wrong Input")
            time.sleep(2)
        else:
            if user_input not in self.user_entery:
                self.user_entery.append(user_input)
                self.chage_values_board(user_input)
            else:
                print("Already exit try another cell ????")
                time.sleep(2)
def clear():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
data = TikTakToe(player1, player2)
winner = True

for i in range(0, 9):
    clear()
    data.user_input()

    if data.winner():
        clear()
        if data.current_value == X_VALUE:
            data.display()
            print(f"Hurray!!! {data.player2} Won.")
        else:
            data.display()
            print(f"Hurray!!! {data.player1} Won.")
        break
    if i == 8:
        print(f"{data.player1} Vs {data.player2} Draw. Better Luck next time")

# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9 ]]
