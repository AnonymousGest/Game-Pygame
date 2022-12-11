import random
from time import *
from tkinter import *
o=0; p=1; list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 45, 50, 60, 70, 80, 90, 100]; list = [2, 3, 5, 10]
window=Tk();window.geometry("1080x720");window.title("Calculator_Game");window.iconbitmap("calculator-logo.ico");window.minsize(420, 360);window.config(background='#2B2B2B')
label_title=Label(window, text="Calculator Game", font=("", 40), bg='#2B2B2B', fg=('white'), bd=1, relief=SUNKEN)
label_title.pack()
frame= Frame(window, bg='#2B2B2B')
label_text=Label(frame, text="Difficulty :", font=("", 25), bg='#2B2B2B', fg=('blue'), bd=1, relief=SUNKEN)
label_text.pack(expand=YES,padx=100)
frame.pack(expand=YES, pady=0)
frame1= Frame(window, bg='#2B2B2B')
frame2= Frame(window, bg='#2B2B2B')
frame3= Frame(window, bg='#2B2B2B')

def generate_easy():
    print("easy")
    sleep(0.2)
    window.destroy()
    sleep(0.7)
def generate_medium():
    print("medium")
    global o
    o+=1
    sleep(0.2)
    window.destroy()
    sleep(0.7)
def generate_hard():
    print("hard")
    global o
    o += 2
    sleep(0.2)
    window.destroy()
    sleep(0.7)
easy_button= Button(frame1, text='• Easy', font=("", 30), bg='blue', fg=('black'), command=generate_easy);easy_button.grid(row=0, column=0)
medium_button= Button(frame2, text='• Medium', font=("", 30), bg='blue', fg=('black'), command=generate_medium);medium_button.grid(row=0, column=0)
hard_button= Button(frame3, text='• Hard', font=("", 30), bg='blue', fg=('black'), command=generate_hard);hard_button.grid(row=0, column=0)

frame1.pack(expand=YES,pady=0)
frame2.pack(expand=YES,pady=0)
frame3.pack(expand=YES,ipady=0)


window.mainloop()


d=1
while 1 == d:
    temps_depart = time()  # mesure le temps en secondes depuis le début du programe et l'inscrit dans la variable temps_depart.
    x=5
    if o==0 or 0==1:
        x = random.randint(0, 2)
    if x == 0:
        if o==0:
            a = random.randint(1, 50)
        else:
            a = random.randint(-49, 49)
            if a==20 or a==30 or a==40 or a==-20 or a==-30 or a==-40:
                a += random.randint(2, 8)
            elif -11<a<-1:
                a+=11
            elif 1<a<11:
                a-=11
            elif a==0:
                list_0=[12,-12]
                a+=random.choice(list_0)
        if o==0:
            b = random.choice(list1)
        elif o==1:
            b = random.randint(13,98)
            if b==20 or b==30 or b==40 or b==50 or b==60 or b==70 or b==80 or b==90:
                b+=random.randint(2,8)
        if o==0 or o==1:
            s = a + b
            c = f"{a}+{b}="
            u = input(c)
    elif x == 1:
        if o==0:
            a = random.randint(1, 50)
        else:
            a = random.randint(11, 99)
        if o==0:
            b = random.randint(1, 10)
        elif o==1:
            b = random.randint(11, 49)
            if b==20 or  b==30 or b==40 or b==25 or b==35 or b==45:
                b+=random.randint(2,4)
        if o == 0 or o == 1:
            s = a - b
            c = f"{a}-{b}="
            u = input(c)
    elif x == 2:
        if o==0:
            a = random.randint(2, 10)
        elif o==1:
            a = random.randint(3, 15)
            if a==10 or a==5:
                a+=random.randint(2,4)
        if o==0:
            b = random.choice(list)
        elif o==1:
            b = random.randint(12,39)
            if b==20 or b==30:
                b+=random.randint(2,8)
        if o==0 or o==1:
            s = a * b
            c = f"{a}*{b}="
            u = input(c)
    if o==2:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if x == 0:
            a = random.randint(-49, 49)
            if a==20 or a==30 or a==40 or a==-20 or a==-30 or a==-40:
                a += random.randint(2, 8)
            elif -11<a<-1:
                a+=11
            elif 1<a<11:
                a-=11
            elif a==0:
                list_0=[12,-12]
                a+=random.choice(list_0)
            else:
                a=a
            b = random.randint(13,98)
            if b==20 or b==30 or b==40 or b==50 or b==60 or b==70 or b==80 or b==90:
                b+=random.randint(2,8)
        if y == 0:
            e = random.randint(-49, 49)
            if e == 20 or e == 30 or e == 40 or e == -20 or e == -30 or e == -40:
                e += random.randint(2, 8)
            elif -11 < e < -1:
                e += 11
            elif 1 < e < 11:
                e -= 11
            elif e == 0:
                list_0 = [12, -12]
                e += random.choice(list_0)
            else:
                e=e
            f = random.randint(13, 98)
            if f == 20 or f == 30 or f == 40 or f == 50 or f == 60 or f == 70 or f == 80 or f == 90:
                f += random.randint(2, 8)
        if x == 1:
            a = random.randint(11, 99)
            b = random.randint(11, 49)
            if b==20 or  b==30 or b==40 or b==25 or b==35 or b==45:
                b+=random.randint(2,4)
        if y == 1:
            e = random.randint(11, 99)
            f = random.randint(11, 49)
            if f == 20 or f == 30 or f == 40 or f == 25 or f == 35 or f == 45:
                f += random.randint(2, 4)
        if x == 2:
            a = random.randint(3, 15)
            if a==10 or a==5:
                a+=random.randint(2,4)
            b = random.randint(12,39)
            if b==20 or b==30:
                b+=random.randint(2,8)
        if y == 2:
            e = random.randint(3, 15)
            if e==10 or e==5:
                e+=random.randint(2,4)
            f = random.randint(12,39)
            if f==20 or f==30:
                f+=random.randint(2,8)
        if x==0 and y==0:
            s = a + b + e + f
            c = f"{a}+{b}+{e}+{f}="
            u = input(c)
        elif x==0 and y==1:
            s = a + b + e - f
            c = f"{a}+{b}+{e}-{f}="
            u = input(c)
        elif x==0 and y==2:
            s = a + b + e * f
            c = f"{a}+{b}+{e}*{f}="
            u = input(c)
        elif x==1 and y==0:
            s = a - b + e + f
            c = f"{a}-{b}+{e}+{f}="
            u = input(c)
        elif x==1 and y==1:
            s = a - b + e - f
            c = f"{a}-{b}+{e}-{f}="
            u = input(c)
        elif x==1 and y==2:
            s = a - b + e * f
            c = f"{a}-{b}+{e}*{f}="
            u = input(c)
        elif x==2 and y==0:
            s = a * b + e + f
            c = f"{a}*{b}+{e}+{f}="
            u = input(c)
        elif x==2 and y==1:
            s = a * b + e - f
            c = f"{a}*{b}+{e}-{f}="
            u = input(c)
        elif x==2 and y==2:
            s = a * b + e * f
            c = f"{a}*{b}+{e}*{f}="
            u = input(c)
    temps_fin = time()  # mesure le temps en secondes depuis le début du programe et l'inscrit dans la variable temps_fin.
    if int(u) == s:
        print("bonne réponse, tu as mis ", round(temps_fin - temps_depart, 2), "sec")
        sleep(0.7)
    else:
        print("perdu !, la réponse était ", s)
        sleep(0.7)
        g = input("tu veux continuer ?")
        if g == "yes" or g == "ok" or g == "pkp" or g == "pqp" or g == "oui" or g == "ouais" or g == "pourquoi pas" or g == "pk pas" or g == "pq pas" or g == "mouais" or g == "moui" or g == "si tu veux" or g == 'stv' or g == "true" or g == "True":
            d = 1
            sleep(0.3)
        else:
            sleep(0.2)
            d = 0
            print("dommage, à +")
            sleep(0.5)