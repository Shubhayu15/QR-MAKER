import qrcode
import tkinter as tk
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter.ttk as ttk
from tkinter import filedialog  # To prompt save file dialog

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x600")

# Set up style with ttkbootstrap
style = Style(theme='superhero')
style.theme_use()

# Global variable to store the QR code image
qr_img = None

# Function to generate and display the QR code
def generate_qr_code():
    global qr_img
    # Get the text entered by the user
    text = text_entry.get()

    # Create a QR code from the text
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the QR code to a format that can be displayed in the Tkinter GUI
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    
    # Update the label with the generated QR code
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk  # Keep a reference to avoid garbage collection
    
    # Store the QR image globally for saving
    qr_img = img

# Function to save the QR code image
def save_qr_code():
    if qr_img:
        # Open file dialog to save the file as PNG
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if file_path:
            # Save the image to the selected file path
            qr_img.save(file_path)
    else:
        print("No QR code to save.")

# Add title label
title_label = ttk.Label(master=root, text="QR CODE GENERATOR APP", style='primary.TLabel', font=("Helvetica", 16))
title_label.pack(pady=20)

# Create input field for text or URL
text_label = ttk.Label(master=root, text="Enter Text or URL:")
text_label.pack(pady=10)
text_entry = ttk.Entry(master=root, width=50)
text_entry.pack()

# Create button to generate QR code
generate_button = ttk.Button(master=root, text="Generate QR Code",
                             command=generate_qr_code, style='success.TButton')
generate_button.pack(pady=10)

# Create a label to display the QR code
qr_label = ttk.Label(master=root)
qr_label.pack(pady=10)

# Create button to save the QR code image
save_button = ttk.Button(master=root, text="Save QR Code",
                         command=save_qr_code, style='primary.TButton')
save_button.pack(pady=10)

# Start the main loop
root.mainloop()
