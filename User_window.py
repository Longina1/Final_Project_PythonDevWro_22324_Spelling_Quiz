import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.8)
root.title('Mistrz ortografii')



label = tk.Label(root, text='Hello', font=('Arial', 20))
label.pack(padx=20, pady=50)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=3)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=3)

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

nextbtn = tk.Button(root, text='Następne')
nextbtn.place(x=100, y=400, height=100, width=100)

exit_button = tk.Button(root, text='Koniec', command=root.quit)
exit_button.place(x=400, y=400, height=100, width=100)
exit_button.pack(ipadx=5, ipady=15, expand=True)

root.mainloop()