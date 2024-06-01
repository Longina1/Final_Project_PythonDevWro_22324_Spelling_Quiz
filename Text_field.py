import tkinter as tk


root = tk.Tk()
window_width = 800
window_height = 600


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centre_x = int(screen_width/2 - window_width / 2)
centre_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(True, True)
root.attributes('-topmost', 1)
root.title('Mistrz ortografii')
root.configure(bg='#FAFAFA')
root.iconbitmap('./Fountain_pen.ico')

questions = ['1. S_wka płomyk_wka szuka oł_wka.',
    '2. Na pla_y tłum się sma_y.',
    '3. Rowe_ysta ze ścieżki ko_ysta.',
    '4. _orobliwie _udy _łopak _odzi powoli.',
    '5. Na _amaku _arcerz chrapie.',
    '6. Zwinna wiewi_rka przebiega przez podw_rka.',
    '7. Bła_ej _ongluje i gumę _uje.',
    '8. B_egiem Bieb_y bóbr szuka wie_by.',
    '9. _ubert w _amaku robi dużo _ałasu.',
    '10. Razu pewnego pszczoła u_ądliła _ółwia _wawego.'
]


answers = ['ó', 'ż', 'rz', 'ch', 'h', 'ó', 'ż', 'rz', 'h', 'ż']

score = 0
total_no_of_questions = 10
question_no = 1


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
        entry.delete('0', tk.END)
        question.config(text=questions[question_no - 1])


frame = tk.Frame(root)
frame.pack(padx=30, pady=10, fill='x', expand=True)

instruction = tk.Label(frame, text='Wpisz literę, której brakuje w poniższym zdaniu.', font=('Verbana', 10), bg='#E0FFFF')
instruction.pack(fill='x', expand=True)

space = tk.Label(frame, text=' \n  \n ', bg='#E0FFFF')
space.pack(fill='x', expand=True)

question = tk.Label(frame, text=questions[question_no - 1], font=('Verbana', 23), bg='#E0FFFF')
question.pack(fill='x', expand=True)

entry_text = tk.StringVar()

entry = tk.Entry(frame, textvariable=entry_text)
entry.pack()

next_button = tk.Button(frame, text='Dalej', command=next, bg='#E0FFFF')
next_button.pack()


root.mainloop()