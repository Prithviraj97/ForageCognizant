import tkinter as tk
from PIL import Image, ImageTk

# Load image
image = Image.open("image.jpg")
photo_image = ImageTk.PhotoImage(image=image)

# Create canvas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Display image
image_id = canvas.create_image(100, 50, image=photo_image)

# Get image coordinates
image_bbox = canvas.bbox(image_id)
image_bottom_y = image_bbox[3]  # Extract bottom-right y coordinate

# Choose text position (adjust as needed)
text_offset = 10  # Add some vertical padding below the image
text_x = image_bbox[0]  # Start text at the same x as the image
text_y = image_bottom_y + text_offset

# Create text element
text_id = canvas.create_text(text_x, text_y, text="Your text here")
