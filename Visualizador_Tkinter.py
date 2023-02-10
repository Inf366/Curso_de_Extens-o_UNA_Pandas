# Autor: GSRS

from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd

#Cria uma tela usando a biblioteca Tkinter
tela = Tk()
tela.geometry("850x650")
tela.title("Projeto de Extensão em Pandas")
tela.pack_propagate(False)
tela.resizable(0,0)

#Módulos
def limpar():
    for item in tv1.get_children():
        tv1.delete(item)

def carregar():
    limpar()
    nome_arquivo = filedialog.askopenfilename(initialdir="/",
                                              title="Selecionar arquivo",
                                              filetype = (("Arquivos xlsx","*.xlsx"),("Qualquer Arquivo",".")))
    arq_lab.delete(0,END)
    arq_lab.insert(0,nome_arquivo)

def carregar_planilha():
    limpar()
    global nome_arquivo
    da = pd.read_excel(arq_lab.get())
    
    #Mudar df para as mudanças na tabela
    
    df = da.head(10)

    #
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end",values=row)

#FrontEnd
frametexto = LabelFrame(tela,text='Tabelas')
framearq = LabelFrame(tela, text="Arquivo Excel")
carregar_botao = Button(tela,text='Abrir Arquivo',command=carregar)
arq_lab = Entry(tela,text=" ",background="white",width=30,font=("Helvetica",12))
carr = Button(tela,command=carregar_planilha,text="Carregar")

frametexto.place(height=620,width=500)
framearq.place(height=200,width=300,relx=0.6,rely=0)
carregar_botao.place(relx=0.605,rely=0.262)
arq_lab.place(relx=0.605,rely=0.08)
carr.place(relx=0.72,rely=0.262)

#TreeView
tv1 = ttk.Treeview(frametexto)
tv1.place(relheight=1,relwidth=1)

scrolly = Scrollbar(frametexto,orient="vertical",command=tv1.yview)
scrollx = Scrollbar(frametexto,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side="bottom",fill="x")
scrolly.pack(side="right",fill="y")


tela.mainloop()
