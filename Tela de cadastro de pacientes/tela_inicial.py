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
from tela_cadastro_consulta import Tela_cadastro_consulta






class Tela_inicial(Tela_cadastro_consulta):
    def tela(self):
        self.root.title("Cadastro de Cliente")
        self.root.configure(background='#1e3743')
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.root.minsize(width=900, height=600)



        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root,
        bd=2,
        bg='#3F515C',
        highlightbackground='#96A1A8',
        highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root,
        bd=2,
        bg='#3F515C',
        highlightbackground='#96A1A8',
        highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):


        # Botão de limpar
        self.bt_limpar = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.02, relwidth=0.1, relheight=0.15)
        self.bt_limpar.configure(text="Limpar",bd=2,activebackground='#96A1A8',activeforeground='#ffffff')

        # Botão de buscar_paciente
        self.bt_buscar = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),command=self.buscar_paciente)
        self.bt_buscar.place(relx=0.3, rely=0.02, relwidth=0.1, relheight=0.15)
        self.bt_buscar.configure(text="Buscar",activebackground='#96A1A8',activeforeground='#ffffff')

        # Botão de novo
        self.bt_novo = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),command=self.Inserir_Dados_pacientes)
        self.bt_novo.place(relx=0.5, rely=0.02, relwidth=0.1, relheight=0.15)
        self.bt_novo.configure(text="Novo",activebackground='#96A1A8',activeforeground='#ffffff')

        # Botão de atualizar
        self.bt_atualizar = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),command=self.atualizar_dados_tabela)
        self.bt_atualizar.place(relx=0.6, rely=0.02, relwidth=0.1, relheight=0.15)
        self.bt_atualizar.configure(text="Atualizar",activebackground='#96A1A8',activeforeground='#ffffff')

        # Botão de excluir
        self.bt_excluir = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'),command=self.apagar_dados_pacientes)
        self.bt_excluir.place(relx=0.7, rely=0.02, relwidth=0.1, relheight=0.15)
        self.bt_excluir.configure(text="Excluir",activebackground='#96A1A8',activeforeground='#ffffff')

        # label de codigo
        self.lb_codigo = Label(self.frame_1)
        self.lb_codigo.place(relx=0.01, rely=0.01)
        self.lb_codigo.configure(text="Código:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de codigo
        self.entry_codigo = Entry(self.frame_1,font=('Arial',15,))
        self.entry_codigo.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.15)

        # label de nome
        self.lb_nome = Label(self.frame_1)
        self.lb_nome.place(relx=0.01, rely=0.33)
        self.lb_nome.configure(text="Nome:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de nome
        self.entry_nome = Entry(self.frame_1,font=('Arial',15,))
        self.entry_nome.place(relx=0.01, rely=0.48, relwidth=0.54, relheight=0.15)

        # label de telefone
        self.lb_telefone = Label(self.frame_1,)
        self.lb_telefone.place(relx=0.01, rely=0.66)
        self.lb_telefone.configure(text="Telefone:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold')) 

        #entry de telefone
        self.entry_telefone = Entry(self.frame_1,font=('Arial',15,))
        self.entry_telefone.place(relx=0.01, rely=0.81, relwidth=0.15, relheight=0.15)

        # label estado civil
        self.lb_estado_civil = Label(self.frame_1)
        self.lb_estado_civil.place(relx=0.2, rely=0.65)
        self.lb_estado_civil.configure(text="Estado Civil:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        #estado civil drop down button
        self.entry_estado_civil = StringVar()
        self.entry_estado_civil.set("Selecione")
        self.estadoC = OptionMenu(self.frame_1, self.entry_estado_civil, "Solteiro", "Casado", "Divorciado", "Viúvo")
        self.estadoC.place(relx=0.2, rely=0.81, relwidth=0.15, relheight=0.15)
        self.estadoC.configure(background="#96A1A8",fg="#F5F4F2",font=('Arial',12,'bold'),highlightthickness=0,highlightbackground='#96A1A8',)
        self.estadoC.configure(text="Novo",activebackground='#96A1A8',activeforeground='#ffffff')

        # label sexo
        self.lb_sexo = Label(self.frame_1)
        self.lb_sexo.place(relx=0.4, rely=0.66)
        self.lb_sexo.configure(text="Sexo:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        # sexo drop down button
        self.entry_sexo = StringVar()
        self.entry_sexo.set("Selecione")
        self.sexoC = OptionMenu(self.frame_1, self.entry_sexo, "Masculino", "Feminino")
        self.sexoC.place(relx=0.4, rely=0.81, relwidth=0.15, relheight=0.16)
        self.sexoC.configure(background="#96A1A8",fg="#F5F4F2",font=('Arial',12,'bold'),highlightthickness=0,highlightbackground='#96A1A8',)
        self.sexoC.configure(text="Novo",activebackground='#96A1A8',activeforeground='#ffffff')

        # calendario
        # label data de nascimento
        self.lb_data_nascimento = Label(self.frame_1)
        self.lb_data_nascimento.place(relx=0.6, rely=0.33)
        self.lb_data_nascimento.configure(text="Data de Nascimento:",background="#3F515C",fg="#F5F4F2",font=('Arial',12,'bold'))

        # botao calendario
        self.bt_data_nascimento = Button(self.frame_1,relief=RAISED,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'), command=self.calendario)
        self.bt_data_nascimento.place(relx=0.8, rely=0.48, relwidth=0.15, relheight=0.15)
        self.bt_data_nascimento.configure(text="Calendario",activebackground='#96A1A8',activeforeground='#ffffff')

        # entry calendario
        self.entry_data_nascimento = Entry(self.frame_1,font=('Arial',15,))
        self.entry_data_nascimento.place(relx=0.6, rely=0.48, relwidth=0.15, relheight=0.15)






    def widgets_frame2(self):

        # gerando tabela
        self.treeview = Treeview(self.frame_2,height=3,columns=('codigo','nome','telefone','sexo','estado_civil','data_nascimento'))
        self.treeview.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)

        #aumentando a fonte da tabela
        style = Style()
        style.configure("Treeview.Heading", font=("Arial", 12,))
        style.configure("Treeview", font=("Arial", 12))

        # cabeçalho da tabela
        self.treeview.heading('#0',text='')
        self.treeview.heading('#1',text='Código')
        self.treeview.heading('#2',text='Nome')
        self.treeview.heading('#3',text='Telefone')
        self.treeview.heading('#4',text='Sexo')
        self.treeview.heading('#5',text='Estado Civil')
        self.treeview.heading('#6',text='Data de Nascimento')
        
        # tamanho das colunas
        self.treeview.column('#0',width=1)
        self.treeview.column('#1',width=50)
        self.treeview.column('#2',width=190)
        self.treeview.column('#3',width=100)
        self.treeview.column('#4',width=80)
        self.treeview.column('#5',width=80)
        self.treeview.column('#6',width=140)

        # gerando scrollbar
        self.scrollbar = Scrollbar(self.frame_2,orient="vertical",command=self.treeview.yview)
        self.scrollbar.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.98)
        self.treeview.configure(yscroll=self.scrollbar.set)
        self.treeview.bind('<Double-1>',self.onDoubleclick)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()
        def tela_cadastro():
            self.iniciar_tela_marcar_consulta()

        menubar.add_cascade(label="opções",menu=filemenu)
        menubar.add_cascade(label="relatorios",menu=filemenu2)

        filemenu.add_command(label="sair",command=Quit)
        filemenu.add_command(label="marcar consulta",command=tela_cadastro)
        filemenu2.add_command(label="ficha do cliente",command=self.geraRelatorioCliente)

    def gerar_tela_prinpipal(self):
        self.tela() 
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.Monta_Tabela_pacientes()
        self.select_lista_pacientes()
        self.menus()

