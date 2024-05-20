import tkinter as tk

def raise_frame():
    frame.tkraise()

root = tk.Tk()
root.geometry('500x600')



start = tk.Frame(root)
page1 = tk.Frame(start)
page2 = tk.Frame(page1)
page3 = tk.Frame(page2)
page4 = tk.Frame(page3)
page5 = tk.Frame(page4)
page6 = tk.Frame(page5)
page7 = tk.Frame(page6)
page8 = tk.Frame(page7)
page9 = tk.Frame(page8)
page10 = tk.Frame(page9)
page11 = tk.Frame(page10)

for frame in (start, page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11):
    # frame.grid(row=0, column=0, sticky='news')

label1 = tk.Label(start, text='Start')
label1.pack()
btn1 = tk.Button(start, text='Dalej', command=lambda:raise_frame()).pack()

label2 = tk.Label(page1, text='Pytanie 2')
label2.pack()
btn2 = tk.Button(page1, text='Dalej', command=lambda:raise_frame()).pack()

label3 = tk.Label(page2, text='Pytanie 2')
label3.pack()
btn3 = tk.Button(page2, text='Dalej', command=lambda:raise_frame()).pack()

label4 = tk.Label(page3, text='Pytanie 3')
label4.pack()
btn4 = tk.Button(page3, text='Dalej', command=lambda:raise_frame()).pack()

label5 = tk.Label(page4, text='Pytanie 4')
label5.pack()
btn5 = tk.Button(page4, text='Dalej', command=lambda:raise_frame()).pack()

label6 = tk.Label(page5, text='Pytanie 5')
label6.pack()
btn6 = tk.Button(page5, text='Dalej', command=lambda:raise_frame()).pack()

label7 = tk.Label(page6, text='Pytanie 6')
label7.pack()
btn7 = tk.Button(page6, text='Dalej', command=lambda:raise_frame()).pack()

label8 = tk.Label(page7, text='Pytanie 7')
label8.pack()
btn8 = tk.Button(page7, text='Dalej', command=lambda:raise_frame()).pack()

label9 = tk.Label(page8, text='Pytanie 8')
label9.pack()
btn9 = tk.Button(page8, text='Dalej', command=lambda:raise_frame()).pack()

label10 = tk.Label(page9, text='Pytanie 9')
label10.pack()
btn10 = tk.Button(page9, text='Dalej', command=lambda:raise_frame()).pack()

label11 = tk.Label(page10, text='Pytanie 10')
label11.pack()
btn11 = tk.Button(page10, text='Jeszcze raz', command=lambda:raise_frame()).pack()


root.mainloop()

