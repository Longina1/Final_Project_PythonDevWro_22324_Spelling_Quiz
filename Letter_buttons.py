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

answers = ['ó', 'ż', 'ż', 'ch', 'ch', 'ó', 'ż', 'rz', 'ż', 'rz']

score = 0
total_no_of_questions = 10
question_no = 1


# Create the calculator display screen
# display_label = tk.Label(root, textvariable=display, font=("Arial", 24), anchor="e", background="white")
# display_label.grid(row=0, column=0, columnspan=4)

def update_textbox(letter):
    global entry_text
    current_text = entry_text.get()
    #textbox.config(state=tk.NORMAL)
    output_textbox.insert('1.0', current_text)
    # textbox.insert('1.0', current_text)

    # global entry_text
    # current_text = entry_text.get()
    # if current_text:
    #    textbox.set(current_text)
    # else:
    #    textbox.set('')

# def click():
#     current_char = entry_text.get()
#     entry_text.set(current_char)




def check():
    pass


# question = tk.Label(root, font=('Arial', 25), bg='#E0F7FA', text=questions[0])
# question.pack(fill=tk.X)

# label = tk.Label(root, text='Mistrz ortografii', font=('Arial', 20))
# label.pack(padx=20, pady=50)
# textbox = tk.Text(root, height=3, font=('Arial', 14))
# textbox.pack(padx=10, pady=10)
# entry_label = tk.Label(root, textvariable=entry_text, anchor='e')
# # entry_label.pack()
# display = tk.Entry(root)
# display.pack()

def next():
    global score,question_no

    if entry_text.get().lower() == answers[question_no - 1]:
        score += 1

    question_no += 1

    if question_no > total_no_of_questions:
        next_button.pack_forget()
        label = tk.Label(root, text='Twój wynik: '+ str(score), font=('Verbana', 30), bg='#FFFAFA', fg='#2F4F4F')
        label.pack(padx=50, pady=50)
        quit_button = tk.Button(root, text='Koniec', command=root.quit, bg='#FFE4E1')
        quit_button.pack(ipadx=5, ipady=15, expand=True)

    else:
        output_textbox.delete('0', tk.END)
        question.config(text=questions[question_no - 1])


output_frame = tk.Frame(root)
output_frame.pack(fill='x')
output_textbox = tk.Text(root, height=3, font=('Arial', 14))
output_textbox.pack(padx=10, pady=10)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='u', font=('Arial', 15), command=lambda letter=button: update_textbox(letter))
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
frame = tk.Frame(root)
frame.pack(padx=30, pady=10, fill='x', expand=True)
next_button = tk.Button(frame, text='Dalej', command=next, bg='#E0FFFF')
next_button.pack()

# exit_button = tk.Button(root, text='Koniec', command=root.quit)
# exit_button.place(x=400, y=400, height=300, width=300)
# exit_button.pack(ipadx=5, ipady=15, expand=True)

root.mainloop()

#btn.pack(side=BOTTOM, anchor="e", padx=8, pady=8)