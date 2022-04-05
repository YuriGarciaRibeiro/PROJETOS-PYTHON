from ast import Str
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from funcs import Funcs



class Tela_cadastro_consulta(Funcs):
    def tela_cadastro(self):
        #configurações da tela
        self.root.title("Cadastro de Cliente")
        self.root.configure(background='#1e3743')
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.root.minsize(width=900, height=600)
    
    def frames_da_tela_cadastro(self):

        # Frame 1
        self.frame_1 = Frame(self.root,
        bd=2,
        bg='#3F515C',
        highlightbackground='#96A1A8',
        highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        # Frame 2
        self.frame_2 = Frame(self.root,
        bd=2,
        bg='#3F515C',
        highlightbackground='#96A1A8',
        highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1_tela_cadastro(self):
        #widgets do frame 1

        # label de codigo
        self.lb_codigo = Label(self.frame_1)
        self.lb_codigo.place(relx=0.01, rely=0.01)
        self.lb_codigo.configure(text="Código:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de codigo
        self.entry_codigo = Entry(self.frame_1,font=('Arial',15,))
        self.entry_codigo.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.15)

        # label de nome
        self.lb_nome = Label(self.frame_1)
        self.lb_nome.place(relx=0.2, rely=0.01)
        self.lb_nome.configure(text="Nome:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de nome
        self.entry_nome = Entry(self.frame_1,font=('Arial',15,))
        self.entry_nome.place(relx=0.2, rely=0.15, relwidth=0.54, relheight=0.15)

        # label de telefone
        self.lb_telefone = Label(self.frame_1,)
        self.lb_telefone.place(relx=0.75, rely=0.01)
        self.lb_telefone.configure(text="Telefone:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de telefone
        self.entry_telefone = Entry(self.frame_1,font=('Arial',15,))
        self.entry_telefone.place(relx=0.76, rely=0.15, relwidth=0.15, relheight=0.15)

        # calendario
        # label data de nascimento
        self.lb_data_consulta = Label(self.frame_1)
        self.lb_data_consulta.place(relx=0.6, rely=0.33)
        self.lb_data_consulta.configure(text="Data da Consulta: ",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        # botao calendario
        self.bt_data_consulta = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'), command=self.calendario2)
        self.bt_data_consulta.place(relx=0.8, rely=0.48, relwidth=0.15, relheight=0.15)
        self.bt_data_consulta.configure(text="Calendario",activebackground='#96A1A8',activeforeground='#ffffff')

        # entry calendario
        self.entry_data_consulta = Entry(self.frame_1,font=('Arial',15,))
        self.entry_data_consulta.place(relx=0.6, rely=0.48, relwidth=0.15, relheight=0.15)

        # label hora
        self.lb_hora = Label(self.frame_1)
        self.lb_hora.place(relx=0.6, rely=0.66)
        self.lb_hora.configure(text="Hora:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        # entry hora
        self.entry_hora = Entry(self.frame_1,font=('Arial',15,))
        self.entry_hora.place(relx=0.6, rely=0.81, relwidth=0.15, relheight=0.15)

        # label de observacao
        self.lb_observacao = Label(self.frame_1)
        self.lb_observacao.place(relx=0.01, rely=0.33)
        self.lb_observacao.configure(text="Observação:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        # entry de observacao
        self.entry_observacao = Entry(self.frame_1,font=('Arial',15,),justify="left")
        self.entry_observacao.place(relx=0.01, rely=0.48, relwidth=0.54, relheight=0.475)

        # botao salvar
        self.bt_salvar = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),text="Salvar Consulta", command=self.inserir_dados_tabela_consultas)
        self.bt_salvar.place(relx=0.8, rely=0.81, relwidth=0.15, relheight=0.15)

    def widgets_frame2_tela_cadastro(self):
        
        
        #widgets do frame 2
        #treeview
        #cria a treeview
        self.treeview = ttk.Treeview(self.frame_2,columns=('Codigo','Nome','Telefone','Data','Hora','Observação'))
        self.treeview.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)

        #configura a treeview
        style = Style()
        style.configure("Treeview.Heading", font=("Arial", 12,))
        style.configure("Treeview", font=("Arial", 12))

        # cabecalho da treeview
        self.treeview.heading('#0',text='')
        self.treeview.heading('#1', text='Código')
        self.treeview.heading('#2', text='Nome')
        self.treeview.heading('#3', text='Telefone')
        self.treeview.heading('#4', text='Data')
        self.treeview.heading('#5', text='Hora')
        self.treeview.heading('#6', text='Observação')

        #tamanho das colunas
        self.treeview.column('#0', width=1)
        self.treeview.column('#1',width=50)
        self.treeview.column('#2',width=190)
        self.treeview.column('#3',width=100)
        self.treeview.column('#4',width=80)
        self.treeview.column('#5',width=80)
        self.treeview.column('#6',width=140)

        #scrollbar
        self.scrollbar = Scrollbar(self.frame_2, orient="vertical", command=self.treeview.yview)
        self.scrollbar.place(relx=0.98, rely=0.01, relheight=0.98)
        self.treeview.configure(yscroll=self.scrollbar.set)
        self.treeview.bind('<Double-1>',self.onDoubleclick)

    def menus2(self):
        menubar2 = Menu(self.root)
        self.root.config(menu=menubar2)
        filemenu = Menu(menubar2)
        filemenu2 = Menu(menubar2)

        def Quit(): self.root.destroy()

        menubar2.add_cascade(label="opções",menu=filemenu)
        menubar2.add_cascade(label="relatorios",menu=filemenu2)

        filemenu.add_command(label="sair",command=Quit)
        filemenu.add_command(label="Cadastrar Cliente")
        filemenu2.add_command(label="ficha do cliente",command=self.geraRelatorioCliente)
    
    def iniciar_tela_marcar_consulta(self):
        self.root = Tk()
        self.tela_cadastro()
        self.frames_da_tela_cadastro()
        self.widgets_frame1_tela_cadastro()
        self.widgets_frame2_tela_cadastro()
        self.montar_tabela_consultas()
        self.select_lista_consultas()
        self.menus2()
        self.root.mainloop()
        
        