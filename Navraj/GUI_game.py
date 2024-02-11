import tkinter as tk
from CardGame import Card, PictureCard, Deck
import os
class CardGameGUI:
    def __init__(self, deck):
        self.deck = deck
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.card_images = {}
        self.card_instances = []
        self.load_card_images()
        self.play_game()

    def load_card_images(self):
        for suit in Card.POSSIBLESUITS:
            for number in range(2, 11):
                card = PictureCard(number, suit)
                self.card_instances.append(card)
                imagefile = card.get_imagefile()
                dir = "C:\\Users\\TheEarthG\\Downloads\\ForageCognizant\\Navraj\\CardGame\\images"
                path = os.path.join(dir, imagefile)
                self.card_images[(number, suit)] = tk.PhotoImage(file=path)

    def play_game(self):
        while self.deck.size() >= 2:
            playercard = self.deck.draw()
            computercard = self.deck.draw()

            self.canvas.delete("all")
            self.display_card(playercard, 100, 100)
            self.display_card(computercard, 100, 100)

            if playercard > computercard:
                self.canvas.create_text(350, 450, text="I WIN")
            elif playercard < computercard:
                self.canvas.create_text(350, 450, text="YOU WIN")
            else:
                self.canvas.create_text(350, 450, text="It's a tie")

            self.root.update()

            playagain = input("Would you like to play again? (y/n): ").lower()
            if playagain != "y":
                break

        if self.deck.size() < 2:
            self.canvas.create_text(350, 450, text="Not enough cards to play.")
            self.root.update()

    def display_card(self, card, x, y):
        number = card.number
        suit = card.suit
        # imagefile = self.card_instances[number-2 and suit].get_imagefile()
        image = self.card_images[(number, suit)]
        self.canvas.create_image(x, y, image=image, anchor=tk.CENTER)

if __name__ == "__main__":
    deck = Deck()
    game = CardGameGUI(deck)
    game.root.mainloop()