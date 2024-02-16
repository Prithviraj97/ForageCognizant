import tkinter as tk
from CardGame import Card, PictureCard, Deck, Game
from PIL import Image, ImageTk
import os
MAX_CARD_WIDTH = 50  # Maximum width for the card images (adjust as needed)
CARD_HEIGHT_RATIO = 1.4  # Aspect ratio of the card images (height / width)
PADDING = 10
class CardGameGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Card Game")
        self.game = Game()
        self.deck = Deck()
        # self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=1200, height=800)
        self.canvas.pack()
        self.card_images = {}
        self.card_instances = []
        self.load_card_images()
        self.play_game()
        

        # Create widgets
        self.play_button = tk.Button(root, text="Play", justify="left",command=self.play_game)
        self.play_button.pack(side=tk.LEFT, padx=PADDING)

        self.restart_button = tk.Button(root, text="Restart", justify="left", command=self.restart)
        self.restart_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(root, text="Quit", justify="right", command=self.quit_game)
        self.quit_button.pack(side=tk.RIGHT)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.player_card_label = tk.Label(root, text="You Picked")
        self.player_card_label.place(relx=1, rely=0, anchor=tk.NE)

        self.computer_card_label = tk.Label(root, text="Computer Picked")
        # self.player_card_label.pack(side=tk.TOP)
        self.computer_card_label.place(relx=0, rely=0, anchor=tk.NW)

    def load_card_images(self):
        for suit in Card.POSSIBLESUITS:
            for number in range(2, 11):
                card = PictureCard(number, suit)
                self.card_instances.append(card)
                imagefile = card._imagefile
                dir = "C:\\Users\\TheEarthG\\Downloads\\ForageCognizant\\Navraj\\CardGame\\images"
                path = os.path.join(dir, imagefile)
                self.card_images[(number, suit)] = tk.PhotoImage(file=path)
        
    
    def play_game(self):
        if self.game.deck.size() < 2:
            self.canvas.create_text(350, 450, text="Not enough cards to play.")
            self.root.update()
            return

        def play_round():
            playercard = self.game.deck.draw()
            computercard = self.game.deck.draw()

            self.canvas.delete("all")
            # self.display_card(playercard, 50, 40)
            # self.display_card(computercard, 300, 40)
            # Calculate maximum width for the card images
            # max_width = min((self.canvas.winfo_width() - 2 * PADDING) / 2, MAX_CARD_WIDTH)

            # # Adjust card sizes if they exceed the maximum width
            # playercard_image = playercard.image.resize((max_width, int(max_width * CARD_HEIGHT_RATIO)), playercard.image.ANTIALIAS)
            # computercard_image = computercard.image.resize((max_width, int(max_width * CARD_HEIGHT_RATIO)), computercard.image.ANTIALIAS)

            # self.display_card(playercard, PADDING, PADDING)
            # self.display_card(computercard, max_width + 2 * PADDING, PADDING)
            self.display_card(computercard, 60, 40)
            self.display_card(playercard, 620, 40)

            if playercard > computercard:
                self.canvas.create_text(580, 790, text="YOU WIN")
            elif playercard < computercard:
                self.canvas.create_text(580, 790, text="I WIN")
            else:
                self.canvas.create_text(580, 790, text="It's a Draw")

            self.root.update()

            # play_again = Game.play(self)
            # self.after(1000, play_round)
        play_round()
                
    def display_card(self, card, x, y):
        number = card.number
        suit = card.suit
        image = self.card_images[(number, suit)]
        
        # image_resize  = Img.resize(Img.width, Img.height // 8)
        # photo = ImageTk.PhotoImage(image_resize)
        self.canvas.create_image(x, y, image=image, anchor=tk.NW)
        # if cardtype:
        #     label = self.player_card_label
        # else:
        #     label = self.computer_card_label
        # label.config(text=f"{card.number} of {card.suit}")
        
        
    def restart(self, photo):
        self.game = Game()
        self.result_label.config(text="")
        # photo = "C:\\Users\\TheEarthG\\Downloads\\ForageCognizant\\Navraj\\CardGame\\images\\default.png"
        self.player_card_label.config(image=photo)
        # self.player_card_image = photo
        # # self.player_card_label.config(image="C:\\Users\\TheEarthG\\Downloads\\ForageCognizant\\Navraj\\CardGame\\images\\default.png")
        # self.computer_card_label.config(image=photo)
        # self.computer_card_image=photo
           

    def quit_game(self):
        self.root.destroy()


if __name__ == "__main__":
    # deck = Deck()
    root = tk.Tk()
    game = CardGameGUI(root)
    game.root.mainloop()

