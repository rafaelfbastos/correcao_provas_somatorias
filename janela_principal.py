from tkinter import *
from tkinter import messagebox
from metodos import *


class JanelaPrincipal:
    """"" Janela Principal da aplicação """""

    def __init__(self):
        self.label_questao = []
        self.gabarito = []
        self.alternativas = []
        self.respostas = []
        self.porcentagem = []

        self.principal = Tk()
        self.principal.title("Correção de Prova Somatoria")

        # Criando os Frames Principais
        self.frame_head = Frame(self.principal)
        self.frame_head.pack()
        self.frame_questao = Frame(self.principal)
        self.frame_questao.pack()
        self.frame_resultado = Frame(self.principal)
        self.frame_resultado.pack(side=RIGHT)

        # Configurando o Header
        Label(self.frame_head, text="Correção de Provas Somatórias", font="Helvetica  14 bold") \
            .grid(row=0, column=0, padx=10, pady=10, columnspan=5)
        Label(self.frame_head, text="Escolha o tipo de prova", font="Helvetica  10") \
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
               command=lambda: messagebox.showinfo("Ajuda",
                                                   "Tipo 1: Proma somatóra onde uma alternativa errada marcada "
                                                   "como certa anula a questão completamente:\n\n\n"
                                                   "Tipo 2: Prova somatória que ultiliza como método de corre"
                                                   "ção a formula:\n\n"
                                                   "Se NPC>NPI\n"
                                                   "P = NP-(NTPC-(NPC-NPI))/NP\n"
                                                   "Se não P=0\n\n"
                                                   "Onde:\n"
                                                   "P – Pontuação do candidato na questão\n"
                                                   "NP – Número de proposições da questão\n"
                                                   "NTPC – Número total de proposições corretas\n"
                                                   "NPC – Número de proposições corretas consideradas corretas pelo candidato\n"
                                                   "NPI – Número de proposições incorretas consideradas corretas pelo candidato\n"
                                                   )).grid(row=1, column=3, padx=5, pady=5)

        # Adicionar as questões

        Label(self.frame_head, text="Quantidade de questões").grid(row=2, column=0, padx=5, pady=5)
        self.img_mais = PhotoImage(file="./img/mais.png")
        self.img_menos = PhotoImage(file="./img/menos.png")
        Button(self.frame_head, image=self.img_mais, anchor=E, command=lambda: self.add_questao()).grid(row=2, column=1)
        Button(self.frame_head, image=self.img_menos, anchor=W, command=lambda: self.remover_questao()).grid(row=2,
                                                                                                             column=2)
        Button(self.frame_head, anchor=W, text="Corrigir", command=lambda: self.corrigir()).grid(row=2, column=3)
        Label(self.frame_questao, text="Questão:", font="Helvetica 10 bold", anchor="center").grid(row=0, column=0,
                                                                                                   padx=5, pady=5)
        Label(self.frame_questao, text="Nº de Alternativas:", font="Helvetica 10 bold", anchor="center").grid(row=0,
                                                                                                              column=1,
                                                                                                              pady=5,
                                                                                                              padx=5)
        Label(self.frame_questao, text="Gabarito:", font="Helvetica 10 bold", anchor="center").grid(row=0, column=2,
                                                                                                    pady=5, padx=5)
        Label(self.frame_questao, text="Resposta:", font="Helvetica 10 bold", anchor="center").grid(row=0, column=3,
                                                                                                    pady=5, padx=5)
        Label(self.frame_questao, text="Porcentagem:", font="Helvetica 10 bold", anchor="center").grid(row=0, column=4,
                                                                                                       pady=5, padx=5)

        # Loop inserindo as questões
        self.add_questao()

        # Bloco do resultado
        Label(self.frame_resultado, text="Resultado:", font="Helvetica 10 bold", anchor="center").pack(side=LEFT,
                                                                                                       padx=5, pady=5)
        self.resultado = Label(self.frame_resultado, text="", background="white", width=15, borderwidth=1,
                               relief="groove")
        self.resultado.pack(side=RIGHT, padx=5, pady=5)

        # fim da janela
        self.principal.mainloop()

    def add_questao(self):
        pos = len(self.label_questao) + 1
        temp = Label(self.frame_questao, text=f'Questão {pos}:', anchor="center")
        self.label_questao.append(temp)
        self.label_questao[-1].grid(row=pos, column=0, padx=5, pady=5)
        temp = Entry(self.frame_questao, width=15)
        self.alternativas.append(temp)
        self.alternativas[-1].grid(row=pos, column=1, padx=5, pady=5)
        temp = Entry(self.frame_questao, width=15)
        self.gabarito.append(temp)
        self.gabarito[-1].grid(row=pos, column=2, padx=5, pady=5)
        temp = Entry(self.frame_questao, width=15)
        self.respostas.append(temp)
        self.respostas[-1].grid(row=pos, column=3, padx=5, pady=5)
        temp = Label(self.frame_questao, text="", background="white", width=15, borderwidth=1, relief="groove")
        self.porcentagem.append(temp)
        self.porcentagem[-1].grid(row=pos, column=4, padx=5, pady=5)

    def remover_questao(self):
        if len(self.label_questao) > 1:
            self.label_questao[-1].destroy()
            del self.label_questao[-1]

            self.alternativas[-1].destroy()
            del self.alternativas[-1]

            self.gabarito[-1].destroy()
            del self.gabarito[-1]

            self.respostas[-1].destroy()
            del self.respostas[-1]

            self.porcentagem[-1].destroy()
            del self.porcentagem[-1]

    def corrigir(self):
        nota = 0

        for i in range(len(self.respostas)):

            try:
                if self.tipo_prova.get() == 1:
                    r = corrigirMetodo1(int(self.gabarito[i].get()), int(self.respostas[i].get()),
                                        int(self.alternativas[i].get()))
                    self.porcentagem[i]["text"] = f"{r:.2%}"

                if self.tipo_prova.get() == 2:
                    r = corrigirMetodo2(int(self.gabarito[i].get()), int(self.respostas[i].get()),
                                        int(self.alternativas[i].get()))
                    self.porcentagem[i]["text"] = f"{r:.2%}"

                nota = nota + r

                nota = nota / len(self.respostas)
                self.resultado["text"] = f'{nota * 10:.1f}'

            except:
                pass
