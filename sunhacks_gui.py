import tkinter as tk

def on_sign_detected(sign_text):
    result_label.config(text="Detected Sign: " + sign_text)

# Define a global variable to track whether Module 1 is pressed
module1_pressed = False

# Define global variables for buttons
button1 = None
button2 = None
button3 = None

def open_menu():
    # Destroy the "Open Menu" button to remove it
    menu_button.destroy()

    # Create a function to build the menu window
    def create_menu_window():
        # Remove the existing elements
        result_label.pack_forget()
        detect_button.pack_forget()

        # Create buttons in the menu window
        global button1, button2, button3
        button1 = tk.Button(app, text="Module 1", command=create_data_input_fields)
        button2 = tk.Button(app, text="Module 2")
        button3 = tk.Button(app, text="Module 3")

        # Place the buttons in the center of the main window with reduced vertical spacing
        button1.grid(row=0, column=0, pady=5)
        button2.grid(row=1, column=0, pady=5)
        button3.grid(row=2, column=0, pady=5)

    # Create a function to build the data input fields
    def create_data_input_fields():
        global module1_pressed

        if button1 is not None:
            button1.grid_forget()
        if button2 is not None:
            button2.grid_forget()
        if button3 is not None:
            button3.grid_forget()

        module1_pressed = True

        # Create two text input fields at the center of the main window
        entry1 = tk.Entry(app)
        entry2 = tk.Entry(app)

        # Place the text input fields at the center of the main window
        entry1.pack()
        entry2.pack()

    create_menu_window()

# Create the main application window with a larger size
app = tk.Tk()
app.title("Sign Language Translator")
app.geometry("600x400")  # Set the window size to 600x400 pixels

# Create a label to display detected sign text
result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Create a button to start sign detection
detect_button = tk.Button(app, text="Detect Sign Language", command=lambda: on_sign_detected("Hello World"))
detect_button.pack()

# Create a button to open the menu and place it in the lower right corner
menu_button = tk.Button(app, text="Open Menu", command=open_menu)
menu_button.place(x=500, y=350)  # Adjust the x and y coordinates as needed

# Center the buttons in the window
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

# Start the GUI application
app.mainloop()
