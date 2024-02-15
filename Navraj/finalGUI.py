import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from CardGame import *

class CardGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Card Game")
        self.card_instances = []
        self.card_images = {}
        self.game = Game()
        self.canvas = tk.Canvas(self.master, width=800, height=800)
        self.canvas.pack()
        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game)
        self.quit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.player_card_label = tk.Label(master)
        self.player_card_label.pack()

        self.computer_card_label = tk.Label(master)
        self.computer_card_label.pack()

    def play(self):
        if self.game.deck.size() < 2:
            messagebox.showinfo("Info", "Not enough cards to play.")
            self.master.destroy()
            return

        playercard = self.game.deck.draw()
        computercard = self.game.deck.draw()

        player_image = self.load_card_image(playercard.imagefile)
        self.player_card_label.config(image=player_image)
        self.player_card_label.image = player_image

        computer_image = self.load_card_image(computercard.imagefile)
        self.computer_card_label.config(image=computer_image)
        self.computer_card_label.image = computer_image

        if playercard > computercard:
            result = "YOU WIN"
        elif playercard < computercard:
            result = "I WIN"
        else:
            result = "It's a tie"

        self.result_label.config(text=result)

    def load_card_image(self, imagefile):
        for suit in Card.POSSIBLESUITS:
            for number in range(2, 11):
                card = PictureCard(number, suit)
                self.card_instances.append(card)
                imagefile = card._imagefile
                dir = "C:\\Users\\TheEarthG\\Downloads\\ForageCognizant\\Navraj\\CardGame\\images"
                path = os.path.join(dir, imagefile)
                self.card_images[(number, suit)] = tk.PhotoImage(file=path)
                try:
                    image = Image.open(path)
                    image = image.resize((100, 150))
                    return ImageTk.PhotoImage(image)
                except FileNotFoundError:
                    return None

    def restart(self):
        self.game = Game()
        self.result_label.config(text="")
        self.player_card_label.config(image="")
        self.computer_card_label.config(image="")

    def quit_game(self):
        self.master.destroy()


if __name__ == "__main__":
    master = tk.Tk()
    app = CardGameGUI(master)
    app.master.mainloop()
