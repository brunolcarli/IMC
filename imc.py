# -*- coding:utf8 -*-

from Tkinter import *





def calculo():
    global frm
    global foto
    frm.destroy()
    frm = Frame(root)
    frm.pack()
    genero = option.get()
    try:
        peso = float(peso_in.get())
        altura = float(altura_in.get())
        if peso >= 0 and altura >= 0:
            imc = peso/(altura**2)
            if genero == 'Masculino':
                if imc < 20.7:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: ABAIXO DO PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="stickman.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 20.7 and imc <= 26.4:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="ideal.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 26.4 and imc <= 27.8:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: MARGINALMENTE ACIMA DO PESO').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="ideal.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 27.8 and imc <= 31.1:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: ACIMA DO PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="obesidade.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 31.1:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: OBESIDADE').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="obesidade.gif")
                    Label(frm, image = foto).pack()

            elif genero == 'Feminino':
                if imc < 19.1:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: ABAIXO DO PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="stickman.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 19.1 or imc <= 25.8:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="ideal.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 25.8 or imc <= 27.3:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: MARGINALMENTE ACIMA DO PESO').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="ideal.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 27.3 or imc <= 32.3:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: ACIMA DO PESO IDEAL').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="obesidade.gif")
                    Label(frm, image = foto).pack()
                elif imc >= 32.3:
                    Label(frm, text='-----------------------------------------------').pack()
                    Label(frm, text='Situação: OBESIDADE').pack()
                    Label(frm, text='-----------------------------------------------').pack()
                    foto = PhotoImage(file="obesidade.gif")
                    Label(frm, image = foto).pack()

					
               
            Label(frm, text='IMC = %.2f' % imc).pack()
    except:
        Label(frm, text='-----------------------------------------------').pack()
        Label(frm, text='(1) Insira um numero').pack()
        Label(frm, text='(2) Utilize . (ponto) ao invés de , (vírgola)').pack()
        Label(frm, text='-----------------------------------------------').pack()
        foto = PhotoImage(file="imc.gif")
        Label(frm, image = foto).pack()



app = Tk()
app.title('IMC')
app.geometry("300x500+100+100")
root = Frame(app)
root.pack()
Label(root, text='IMC').pack()
Label(root, text='Insira seu peso').pack()
peso_in = Entry(root)
peso_in.pack()
Label(root, text='Insira sua altura').pack()
altura_in = Entry(root)
altura_in.pack()

option = StringVar()
opcoes = ['Masculino', 'Feminino']
OptionMenu(root, option, *opcoes).pack()
option.set(opcoes[0])


btn = Button(root, text='Confirma', command=calculo, bg = "white")
btn.pack()

frm = Frame(root)
frm.pack()

foto = PhotoImage(file="imc.gif")
Label(frm, image = foto).pack()






app.mainloop()
