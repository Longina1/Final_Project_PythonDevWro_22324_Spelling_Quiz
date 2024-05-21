import tkinter as tk

root = tk.Tk()
window_width = 800
window_height = 600


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

frame = tk.Frame()
frame.pack()

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

options = [['u', 'ó'],
            ['ż', 'rz'],
            ['rz', 'ż'],
            ['h', 'ch'],
            ['ch', 'h'],
            ['ó', 'u'],
            ['ż', 'rz'],
            ['rz', 'ż'],
            ['ż', 'rz'],
            ['rz', 'ż']
]



answers = [2, 1, 2, 2, 1, 1, 1, 1, 1, 1]

score = 0
total_no_of_questions = 10
question_no = 1


def next():
    global score,question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    else:
        selected_option = -1

    if answers[question_no - 1] == selected_option:
        score += 1

    question_no += 1

    if question_no > total_no_of_questions:
        next_btn.pack_forget()
        label = tk.Label(root, text='Twój wynik: '+ str(score), font=('Arial', 30), bg='#84FFFF')
        label.pack(padx=20, pady=20)

    else:
        val1.set(0)
        val2.set(0)
        question.config(text=questions[question_no - 1])
        option1.config(text=options[question_no - 1][0])
        option2.config(text=options[question_no - 1][1])



def check(option):
    if option == 1:
        val2.set(0)
    else:
        val1.set(0)


question = tk.Label(root, font=('Arial', 25), bg='#E0F7FA', text=questions[0])
question.pack(fill=tk.X)

val1 = tk.IntVar()
val2 = tk.IntVar()

option1 = tk.Checkbutton(root, variable=val1, text=options[0][0], font=('Arial', 20), bg='#FAFAFA', command=lambda:check(1))
option1.pack()

option2 = tk.Checkbutton(root, variable=val2, text=options[0][1], font=('Arial', 20), bg='#FAFAFA', command=lambda: check(2))
option2.pack()

next_btn = tk.Button(root, text='Dalej', bg='#BBDEFB', command=next)
next_btn.pack()


root.mainloop()