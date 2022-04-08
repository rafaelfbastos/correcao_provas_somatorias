from tkinter import *
from tkinter import messagebox


class JanelaPrincipal:

    """"" Janela Principal da aplicação """""

    def __init__(self):
        self.principal = Tk()
        self.principal.title("Correção de Prova Somatoria")

        # Criando os Frames Principais
        self.frame_head = Frame(self.principal)
        self.frame_head.pack(side=TOP, expand=TRUE, fill=BOTH)
        self.frame_questao = Frame(self.principal)
        self.frame_questao.pack(side=BOTTOM, expand=TRUE, fill=BOTH)

        # Configurando o Header
        Label(self.frame_head, text="Correçào de Provas Somatórias", font="Helvetica  14 bold")\
            .grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        Label(self.frame_head, text="Ecolha tipo de prova", font="Helvetica  10")\
            .grid(row=1, column=0, padx=5, pady=5)

        # Configurando Radio Botton
        self.tipo_prova = IntVar()
        self.rb_t1 = Radiobutton(self.frame_head, text="Tipo 1", value=1, variable=self.tipo_prova)
        self.rb_t1.grid(row=1, column=1, padx=5, pady=5)
        self.rb_t2 = Radiobutton(self.frame_head, text="Tipo 2", value=2, variable=self.tipo_prova)
        self.rb_t2.grid(row=1, column=2, padx=5, pady=5)
        # Butão de ajuda falta iplementar
        self.img_ajuda = PhotoImage(file="./img/ajuda.png")
        Button(self.frame_head, image=self.img_ajuda,
               command=lambda: messagebox.showinfo("showinfo", "Information")).grid(row=1, column=3, padx=5, pady=5)

        # Adicionar as questões
        Label(self.frame_head, text="Quantidade de questões").grid(row=2, column=0, padx=5, pady=5)
        self.img_mais = PhotoImage(file="./img/mais.png")
        self.img_menos = PhotoImage(file="./img/menos.png")
        self.btn_mais = Button(self.frame_head, image=self.img_mais, anchor=E).grid(row=2, column=1)
        self.btn_menos = Button(self.frame_head, image=self.img_menos, anchor=W).grid(row=2, column=2)



        self.principal.mainloop()
