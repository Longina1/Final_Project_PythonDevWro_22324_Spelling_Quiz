import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
# root.geometry('500x600')
window_width = 800
window_height = 600


#pobieranie wielkości ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#print(screen_width, screen_height)
centre_x = int(screen_width/2 - window_width / 2)
centre_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.8)
root.title('Mistrz ortografii')
root.iconbitmap('./Fountain_pen.ico')

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

entry_text = tk.StringVar()
entry_text.set('')


def click():
    current_char = entry_text.get()
    entry_text.set(current_char)

def next():
    pass


def check():
    pass

question = tk.Label(root, font=('Arial', 25), bg='#E0F7FA', text=questions[0])
question.pack(fill=tk.X)

# label = tk.Label(root, text='Mistrz ortografii', font=('Arial', 20))
# label.pack(padx=20, pady=50)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=10)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='u', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=10)
btn2 = tk.Button(buttonframe, text='ó', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=10)
btn3 = tk.Button(buttonframe, text='rz', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=10)
btn4 = tk.Button(buttonframe, text='ż', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, padx=10)
btn5 = tk.Button(buttonframe, text='h', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=10)
btn6 = tk.Button(buttonframe, text='ch', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=10)
buttonframe.pack(fill='x')



# for btn in (btn1, btn2, btn3, btn4, btn5, btn6):
#
#
#     def button_clicked():
#         showinfo(title='Potwierdzenie', message='Potwierdź swój wybór')
#
#     button_icon = tk.Button(btn)
#     button = tk.Button(root, image=button_icon, command=button_clicked())
#
# button_icon = tk.PhotoImage(file='../Merito.png')
#
# button = tk.Button(root, image=button_icon, command=button_clicked)
# button.pack(ipadx=5, ipady=5,expand=True) #expand True - zawsze na środku

next_btn = tk.Button(root, text='Następne')
next_btn.place(x=300, y=300, height=100, width=100)

# exit_button = tk.Button(root, text='Koniec', command=root.quit)
# exit_button.place(x=400, y=400, height=300, width=300)
# exit_button.pack(ipadx=5, ipady=15, expand=True)

root.mainloop()

#btn.pack(side=BOTTOM, anchor="e", padx=8, pady=8)