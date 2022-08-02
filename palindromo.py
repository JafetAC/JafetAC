# Proyectos de Palindromos

from tkinter import *;

raiz = Tk();
raiz.title("Palíndromos");
raiz.geometry("350x115");
raiz.config(bg="white");
text1 = '';

def palindromo():
    lista = T.get();
    l = lista;
    c=0;
    for i in reversed(l):
        if(i != lista[c]):
            label2.config(text="No es palindromo");
            label2.pack(ipadx=10, ipady=10);
            break;
        c+=1;
        if(c == len(l)):
            label2.config(text="Es palindromo");
            label2.pack(ipadx=10, ipady=10);


label = Label(raiz, text="Inserte una palabra o oración: ", font=("Arial", 12));
label.pack(ipadx=5, ipady=6);

T = Entry(raiz);
T.pack(ipadx=50);
T.focus_set();

b1 = Button(raiz, text = "OK", command=palindromo);
b1.pack();

label2 = Label(raiz, text=text1, font=("Arial", 10));


raiz.mainloop();




