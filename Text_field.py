import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
window_width = 800
window_height = 600
entry_text = tk.StringVar()

#pobieranie wielkości ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#print(screen_width, screen_height)
centre_x = int(screen_width/2 - window_width / 2)
centre_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(True, True)
root.attributes('-topmost', 1)
# root.attributes('-alpha', 0.8)
root.title('Mistrz ortografii')
root.configure(bg='#FAFAFA')
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


answers = ['ó', 'ż', 'ż', 'ch', 'ch', 'ó', 'ż', 'rz', 'ż', 'rz']

score = 0
total_no_of_questions = 10
question_no = 1

# def button_clicked():
#     msg = f'Brakuje litery: {entry_text.get()}'
#     showinfo(title='Odpowiedź', message=msg)


# def delete_text():
#     entry.delete('1.0', tk.END)


def next():
    global score,question_no
    # if val1.get() == 1:
    #     selected_option = 1
    # elif val2.get() == 1:
    #     selected_option = 2
    # else:
    #     selected_option = -1

    if entry_text.get().lower() == answers[question_no - 1]:
        score += 1

    question_no += 1

    if question_no > total_no_of_questions:
        button.pack_forget()
        label = tk.Label(root, text='Twój wynik: '+ str(score), font=('Verbana', 30), fg='#2F4F4F')
        label.pack(padx=50, pady=50)

    else:
    #     val1.set(0)
    #     val2.set(0)
        entry.delete('0', tk.END)
        question.config(text=questions[question_no - 1])
        # option1.config(text=options[question_no - 1][0])
        # option2.config(text=options[question_no - 1][1])


frame = tk.Frame(root)
frame.pack(padx=30, pady=10, fill='x', expand=True) #ramka w środku; pad - obramowanie

instruction = tk.Label(frame, text='Wpisz literę, której brakuje w poniższym zdaniu.', font=('Verbana', 10), bg='#E0FFFF') #obiekt kalsy Label
instruction.pack(fill='x', expand=True)

space = tk.Label(frame, text=' \n  \n ', bg='#E0FFFF') #obiekt kalsy Label
space.pack(fill='x', expand=True)

question = tk.Label(frame, text=questions[question_no - 1], font=('Verbana', 25), bg='#E0FFFF') #obiekt kalsy Label
question.pack(fill='x', expand=True)

entry = tk.Entry(frame, textvariable=entry_text) #pole tekstowe do wpisywania
entry.pack()

button = tk.Button(frame, text='Dalej', command=next, bg='#E0FFFF')
button.pack() #ramka na całą szeerokość i label na całą szerokość ramki; pady - przycisk będzie niżej

# next_button = tk.Button(frame, text='Dalej', command=next)
# next_button.pack()

root.mainloop()