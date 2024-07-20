from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("XOX")
root.geometry("320x660")
b_click = True
click_button_list = []
x_puan = 0
y_puan = 0

def winner():
    global y_puan, x_puan, click_button_list
    if y_puan == 3:
        messagebox.showinfo("Galip", "O oyuncusu oyunun galibi")
        rtrn()
    elif x_puan == 3:
        messagebox.showinfo("Galip", "X oyuncusu oyunun galibi")
        rtrn()
    else:
        for buttons in click_button_list:
            buttons["text"] = " "
        click_button_list = []

def rtrn():
    global click_button_list, x_puan, y_puan
    tekrar = messagebox.askquestion("XOX", "Tekrar oynamak ister misiniz?")
    if tekrar == "yes":
        for buttons in click_button_list:
            buttons["text"] = " "
        click_button_list = []
        x_puan = 0
        y_puan = 0
        skor()
    else:
        root.destroy()

def xox(buttons):
    global x_puan, y_puan
    global b_click
    click_button_list.append(buttons)
    if buttons["text"] == " " and b_click == True:
        buttons["text"] = "X"
        b_click = False
    elif buttons["text"] == " " and b_click == False:
        buttons["text"] = "O"
        b_click = True

    if ((button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X") or
        (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X") or
        (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X") or
        (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X") or
        (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X") or
        (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X") or
        (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X") or
        (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X")):
        messagebox.showinfo("Kazanan", "X oyuncusu bu turu kazandı")
        x_puan += 1
        b_click = True
        skor()
        winner()
    elif ((button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O") or
          (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O") or
          (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O") or
          (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O") or
          (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O") or
          (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O") or
          (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O") or
          (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O")):
        messagebox.showinfo("Kazanan", "O oyuncusu bu turu kazandı")
        y_puan += 1
        b_click = False
        skor()
        winner()
    elif (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
          button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
          button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):
        messagebox.showinfo("Berabere", "Berabere kaldınız")
        skor()
        winner()
    skor()

def skor():
    global x_puan, y_puan, b_click
    if b_click == True:
        mtn = "X = {} || O = {}".format(x_puan, y_puan)
    else:
        mtn = "X = {} || O = {}".format(x_puan, y_puan)
    skor_tab.config(text=mtn)

# Skor tablosu
skor_tab = Label(root, text="X = 0 || O = 0", font="Arial 20 bold", bd=0, relief=FLAT, anchor=N)
skor_tab.grid(row=0, column=0, columnspan=3, sticky=N)

# Oyun alanı
buttons = StringVar()
button1 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=4, command=lambda: xox(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

cevap = messagebox.askquestion("Soru", "Oyuna X oyuncusu mu başlasın?")
if cevap == "yes":
    b_click = True
else:
    b_click = False
skor()

root.mainloop()
