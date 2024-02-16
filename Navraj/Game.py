from tkinter import *
from PIL import Image, ImageTk
MAX_WIDTH = 140  # Maximum width for the card image
MAX_HEIGHT = 150
# Define the image path
image_path = "Navraj\CardGame\images\queen_of_hearts.png"  # Replace with your actual image path

# Create the main window
root = Tk()
root.title("Image Display")

# Load the image using PIL and convert to PhotoImage
image = Image.open(image_path)
# Resize the image while maintaining aspect ratio
image = image.resize((min(image.width, MAX_WIDTH), min(image.height, MAX_HEIGHT)), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

print(image.width, image.height)
# Create a canvas to display the image
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=NW, image=photo)

# Start the event loop
root.mainloop()
