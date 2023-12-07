import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal

class VirtualMouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Mouse Controller")
        self.root.geometry("400x200")  # Set the initial size of the window
        self.root.config(bg="#1E272E")  # Set background color

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14), padding=10, background="#DDE6ED", foreground="#27374D")
        style.configure("TLabel", font=("Helvetica", 16), padding=10, background="#1E272E", foreground="white")

        # Header label
        header_label = ttk.Label(root, text="Virtual Mouse Controller", style="TLabel")
        header_label.pack(pady=10)

        # Start button
        self.start_button = ttk.Button(root, text="Start Virtual Mouse", command=self.start_virtual_mouse, style="TButton")
        self.start_button.pack(pady=20)
        self.start_button.bind("<Enter>", self.on_enter)  # Bind Enter event
        self.start_button.bind("<Leave>", self.on_leave)  # Bind Leave event

        # Quit button
        self.quit_button = ttk.Button(root, text="Quit", command=self.quit_application, style="TButton")
        self.quit_button.pack()

        # Variable to store the process ID of the Virtual_Mouse.py script
        self.mouse_process = None

    def start_virtual_mouse(self):
        # Replace 'Virtual_Mouse.py' with the actual path to your 'Virtual_Mouse.py' script
        self.mouse_process = subprocess.Popen(["python", "src\Virtual_Mouse.py"])

    def on_enter(self, event):
        # Change font color to black when mouse enters the button
        self.start_button['foreground'] = 'black'

    def on_leave(self, event):
        # Change font color to white when mouse leaves the button
        self.start_button['foreground'] = 'white'

    def quit_application(self):
    # Close the Virtual_Mouse.py process gracefully
        if self.mouse_process:
            try:
                # Terminate the process gracefully
                self.mouse_process.terminate()
                self.mouse_process.wait(timeout=2)  # Wait for the process to exit
            except ProcessLookupError:
                pass

        self.root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualMouseApp(root)
    root.mainloop()
