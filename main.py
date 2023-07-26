from tiktaktoe import TikTakToe

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
game = TikTakToe(player1, player2)
while True:
    game.play()
    if input("If you want to over game type: No").upper() == "NO":
        game.result()
        break
