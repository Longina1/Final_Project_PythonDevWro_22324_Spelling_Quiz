import tkinter as tk
# Create a Tkinter window
root = tk.Tk()
root.geometry("720x400")
# Set the window title
root.title("Displaying Numbers in Calculator")
# Create a variable to store the display text
display = tk.StringVar()
display.set("0")

# Create the calculator display screen
display_label = tk.Label(root, textvariable=display, font=("Arial", 24), anchor="e", background="white")
display_label.grid(row=0, column=0, columnspan=4)
# Create buttons for digits and operations
buttons = [
   "7", "8", "9", "/",
   "4", "5", "6", "*",
   "1", "2", "3", "-",
   "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
   tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: update_display(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
   col_val += 1
   if col_val > 3:
      col_val = 0
      row_val += 1
# Function to update the calculator display
def update_display(value):
   current_text = display.get()
   if current_text == "0" or current_text == "Error":
      display.set(value)
   else:
      display.set(current_text + value)

# Function to perform calculations
def calculate():
   try:
      result = eval(display.get())
      display.set(result)
   except:
      display.set("Error")
# Start the Tkinter main loop
root.mainloop()