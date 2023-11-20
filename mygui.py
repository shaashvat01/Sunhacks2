import tkinter as tk
import cv2
from threading import Thread
from PIL import Image, ImageTk
import mediapipe as mp

# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the camera
cap = None
display_video = False

# Create an empty list to store the finger tip path
finger_path = []

def start_camera():
    global cap, display_video
    cap = cv2.VideoCapture(0)
    display_video = True
    video_thread = Thread(target=display_video_feed)
    video_thread.daemon = True
    video_thread.start()

def display_video_feed():
    global display_video
    while display_video and cap is not None and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))

        video_label.config(image=photo)
        video_label.image = photo

def stop_camera():
    global cap, display_video
    display_video = False
    if cap is not None:
        cap.release()

def on_sign_detected(sign_text):
    result_label.config(text="Detected Sign: " + sign_text)

def switch_module(module_num):
    if module_num == 1:
        start_camera()  # Start camera when Module 1 is selected
        # Your module 1 code here
    elif module_num == 2:
        stop_camera()  # Stop camera when switching to Module 2
        # Your module 2 code here
    elif module_num == 3:
        stop_camera()  # Stop camera when switching to Module 3
        # Your module 3 code here

def open_menu():
    menu_button.destroy()

    def create_menu_window():
        result_label.pack_forget()
        detect_button.pack_forget()

        button1 = tk.Button(app, text="Module 1", command=lambda: switch_module(1))
        button2 = tk.Button(app, text="Module 2", command=lambda: switch_module(2))
        button3 = tk.Button(app, text="Module 3", command=lambda: switch_module(3))

        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)

    create_menu_window()

app = tk.Tk()
app.title("Sign Language Translator")
app.geometry("800x600")  # Set the window size to 800x600 pixels

result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

detect_button = tk.Button(app, text="Detect Sign Language", command=lambda: on_sign_detected("Hello World"))
detect_button.pack()

video_label = tk.Label(app)
video_label.pack(pady=20)

menu_button = tk.Button(app, text="Open Menu", command=open_menu)
menu_button.place(x=700, y=550)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()
