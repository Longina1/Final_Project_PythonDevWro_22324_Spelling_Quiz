import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
window_width = 800
window_height = 600


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centre_x = int(screen_width/2 - window_width / 2)
centre_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.title('Mistrz ortografii')
root.iconbitmap('./Fountain_pen.ico')

entry_text = tk.StringVar()


questions = ['1. St_ł bez n_g chowam za r_g.',
    '2. _urawie _erują w trawie.',
    '3. _ółta _aba szuka kraba.',
    '4. Czy _arty mają duży hart du_a?',
    '5. Mu_a nie wypełni brzu_a żuka.',
    '6. R_żowa k_zka weszła do w_zka.',
    '7. Ły_ka i ły_eczka, a do tego fili_aneczka.',
    '8. Kto bazg_e po mu_e zamiast wycierać ku_e?',
    '9. Ka_dy mo_e jechać nad morze.',
    '10. Na d_ewie mieszka zwie_ę.'
]

display_label = tk.Label(root, textvariable=entry_text, font=("Arial", 24), anchor="e", background="white")
display_label.grid(row=0, column=0, columnspan=3)



def update_textbox():
    global entry_text
    current_text = entry_text.get()





button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text='u', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=10)
btn2 = tk.Button(button_frame, text='ó', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=10)
btn3 = tk.Button(button_frame, text='rz', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=10)
btn4 = tk.Button(button_frame, text='ż', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, padx=10)
btn5 = tk.Button(button_frame, text='h', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=10)
btn6 = tk.Button(button_frame, text='ch', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=10)
# button_frame.pack(fill='x')
button_frame.grid(row=3, column=3)



next_btn = tk.Button(root, text='Następne')
next_btn.place(x=300, y=300, height=100, width=100)


root.mainloop()