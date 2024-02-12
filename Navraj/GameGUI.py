'''This GUI should be able to show both drawn cards and print wining card.'''

import PySimpleGUI as sg
from CardGame import Game

class CardGameGUI:
    def __init__(self):
        self.game = Game()
        self.layout = [
            [sg.Text("Welcome to the Card Game!")],
            [sg.Button("Start Game")],
            [sg.Output(size=(60, 20))]
        ]

    def run(self):
        window = sg.Window("Card Game", self.layout)

        while True:
            event, _ = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Start Game":
                self.play_game(window)

        window.close()

    def play_game(self, window):
        window["Start Game"].update(disabled=True)

        while self.game.get_deck().size() >= 2:
            player_card = self.game.get_deck().draw()
            computer_card = self.game.get_deck().draw()

            output = f"Player's card: {player_card}\nComputer's card: {computer_card}\n"

            if player_card > computer_card:
                output += "Player wins!\n"
            elif player_card < computer_card:
                output += "Computer wins!\n"
            else:
                output += "It's a tie!\n"

            window.write(output)

        if self.game.get_deck().size() == 1:
            window.write("There's only one card left in the deck. Not enough cards to continue playing.\n")

        if self.game.get_deck().size() == 0:
            window.write("There are no cards left in the deck. Game over.\n")

        window["Start Game"].update(disabled=False)


if __name__ == "__main__":
    game_gui = CardGameGUI()
    game_gui.run()
