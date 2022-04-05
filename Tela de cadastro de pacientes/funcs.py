from ast import Str
import locale
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import sqlite3
import base64
from tkcalendar import Calendar, DateEntry


class Funcs():
    def dados(self):
        self.cod = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.telefone = self.entry_telefone.get()
        self.sexo = self.entry_sexo.get()
        self.estado_civil = self.entry_estado_civil.get()
        self.data_nascimento = self.entry_data_nascimento.get()
    
    def limpa_tela(self):
        
        # limpa os campos
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_telefone.delete(0, END)
        try:
            self.entry_data_nascimento.delete(0, END)
        except:
            pass
        try:
            self.entry_observacao.delete(0, END)
        except:
            pass
        try:
            self.entry_data_consulta.delete(0, END)
        except:
            pass
        try:
            self.entry_hora.delete(0, END)
        except:
            pass

    def conectar_banco_de_dados_pacientes(self):

        self.conn = sqlite3.connect('clientes.db')
        self.c = self.conn.cursor()

    def desconectar_banco_de_dados_pacientes(self):

        self.conn.close(); print('Desconectado do Banco de Dados')

    def Monta_Tabela_pacientes(self):
        
        # gera a tabela de clientes no banco de dados
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
        self.c.execute("""CREATE TABLE IF NOT EXISTS clientes(
            cod INTEGER PRIMARY KEY,
            nome_cliente char(40) NOT NULL, 
            telefone integer(20),
            estado_civil char(20),
            sexo char(20),
            data_nascimento char(20)
            );""")
        self.conn.commit(); print('Tabela Criada')
        self.desconectar_banco_de_dados_pacientes();

    def Inserir_Dados_pacientes(self):
        # pega os dados dos campos
        self.dados()
        
        # verifica se os dados estão vazios
        if self.nome == '' :
            msg = "Preencha o campo Nome"
            messagebox.showinfo("Aviso", msg)
        elif self.telefone == '' :
            msg = "Preencha o campo Telefone"
            messagebox.showinfo("Aviso", msg)
        else:
            # conecta ao banco de dados e insere os dados
            print(self.estado_civil)
            self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
            self.c.execute("""INSERT INTO clientes(nome_cliente, telefone, sexo, estado_civil, data_nascimento) VALUES(?,?,?,?,?)""",
                        ( self.nome, self.telefone, self.sexo, self.estado_civil, self.data_nascimento))
            self.conn.commit(); print('Dados Inseridos')
            self.desconectar_banco_de_dados_pacientes()
            self.select_lista_pacientes()
            self.limpa_tela()

    def select_lista_pacientes(self):

        # esvazia a treeview
        self.treeview.delete(*self.treeview.get_children())

        # conecta ao banco de dados e seleciona os dados
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
        lista = self.c.execute("""SELECT cod, nome_cliente, telefone, sexo, estado_civil, data_nascimento FROM clientes
            ORDER BY nome_cliente ASC;""")

        # monta a treeview
        for i in lista:
            self.treeview.insert('', END, values=i)
        self.desconectar_banco_de_dados_pacientes()

    def apagar_dados_pacientes(self):
        # pega o codigo do cliente
        self.cod = self.entry_codigo.get()

        # conecta ao banco de dados e apaga os dados
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
        self.c.execute("""DELETE FROM clientes WHERE cod = ?""", (self.cod,))
        

        #atualiza a treeview e tabela
        self.conn.commit(); print('Dados Apagados')
        self.desconectar_banco_de_dados_pacientes()
        self.select_lista_pacientes()
        self.limpa_tela()

    def onDoubleclick(self, event):
        self.limpa_tela()
        self.treeview.selection()

        for n in self.treeview.selection():
            self.cod,self.nome,self.telefone,self.sexo_data,self.estado_civil_hora,self.data_nascimento_obs = self.treeview.item(n,"values")
            self.entry_codigo.insert(END, self.cod)
            self.entry_nome.insert(END, self.nome)
            self.entry_telefone.insert(END, self.telefone)
            try:
                self.entry_data_nascimento.insert(END, self.data_nascimento_obs)
            except:
                pass
            try:
                self.entry_observacao.insert(END, self.data_nascimento_obs)
            except:
                pass
            try:
                self.entry_data_consulta.insert(END, self.sexo_data)
            except:
                pass
            try:
                self.entry_hora.insert(END, self.estado_civil_hora)
            except:
                pass

    def atualizar_dados_tabela(self):
        self.dados()
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
        if self.cod == '':
            msg = "Selecione um cliente"
            messagebox.showinfo("Aviso", msg)
        elif self.nome == '' :
            msg = "Preencha o campo Nome"
            messagebox.showinfo("Aviso", msg)
        elif self.telefone == '' :
            msg = "Preencha o campo Telefone"
            messagebox.showinfo("Aviso", msg)
        else:
            self.c.execute("""UPDATE clientes SET nome_cliente = ?, sexo = ?,  estado_civil = ?,telefone = ?, data_nascimento = ? 
                WHERE cod = ?;""", (self.nome, self.sexo, self.estado_civil,self.telefone,self.data_nascimento,self.cod))
            self.conn.commit(); print('Dados Atualizados')
            self.desconectar_banco_de_dados_pacientes()
            self.select_lista_pacientes()
            self.limpa_tela()

    def buscar_paciente(self):
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')

        # limpando a treeview
        self.treeview.delete(*self.treeview.get_children())

        # seleciona os dados
        self.entry_nome.insert(END, "%")
        nome = self.entry_nome.get()
        self.c.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC;""" % nome)

        lista = self.c.fetchall()

        # monta a treeview
        for i in lista:
            self.treeview.insert('', END, values=i)
        self.limpa_tela()
        self.desconectar_banco_de_dados_pacientes()

    def calendario(self):
        self.calendario1 = Calendar(self.frame_1,locale='pt_BR')
        self.calendario1.place(relx = 0.1, rely = 0.025,relwidth=0.70, relheight=0.90)
        self.calDataInicio = Button(self.frame_1, text='Inserir data',command=self.print_calendario,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'))
        self.calDataInicio.place(relx=0.8, rely=0.68, relwidth=0.15, relheight=0.15)

    def print_calendario(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data_nascimento.delete(0, END)
        self.entry_data_nascimento.insert(END, dataIni)
        self.calDataInicio.destroy()

    def verificar_cadastro_paciente(self):
    
        self.conectar_banco_de_dados_pacientes(); print('Conectado ao Banco de Dados')
        self.c.execute("""SELECT cod FROM clientes WHERE cod = ?""", (self.cod,))
        lista = self.c.fetchall()
        if len(lista) == 0:
            msg = "Cadastre um paciente"
            messagebox.showinfo("Aviso", msg)
        else:
            self.desconectar_banco_de_dados_pacientes()

    def calendario2(self):
        self.calendario0 = Calendar(self.frame_1,locale='pt_BR')
        self.calendario0.place(relx = 0.1, rely = 0.025,relwidth=0.70, relheight=0.90)
        self.calDataInicio = Button(self.frame_1, text='Inserir data',command=self.print_calendario2,bg='#96A1A8',fg='#ffffff',font=('Arial',12,'bold'))
        self.calDataInicio.place(relx=0.8, rely=0.68, relwidth=0.15, relheight=0.15)

    def print_calendario2(self):
        dataIni = self.calendario0.get_date()
        self.calendario0.destroy()
        self.entry_data_consulta.delete(0, END)
        self.entry_data_consulta.insert(END, dataIni)
        self.calDataInicio.destroy()

    def abrir_banco_de_dados_consultas(self):
        self.conn = sqlite3.connect('consultas.db')
        self.c = self.conn.cursor()
    
    def montar_tabela_consultas(self):
        self.abrir_banco_de_dados_consultas()
        self.c.execute("""CREATE TABLE IF NOT EXISTS consultas(
            cod INTEGER PRIMARY KEY,
            nome_cliente char(40) NOT NULL, 
            data_consulta date NOT NULL,
            telefone char(40) NOT NULL,
            observacao char(40) NOT NULL,
            horario char(40) NOT NULL
            );
        """)
        self.conn.commit() ; print('Tabela Criada')
        self.desconectar_banco_de_dados_consultas()

    def select_lista_consultas(self):
        self.abrir_banco_de_dados_consultas()
        self.c.execute("""SELECT cod, nome_cliente, telefone,data_consulta, horario, observacao FROM consultas ORDER BY nome_cliente ASC;""")
        lista = self.c.fetchall()
        for i in lista:
            self.treeview.insert('', END, values=i)
        self.desconectar_banco_de_dados_consultas()

    def desconectar_banco_de_dados_consultas(self):
        self.conn.close()

    def inserir_dados_tabela_consultas(self):
        self.nome = self.entry_nome.get()
        self.data_consulta = self.entry_data_consulta.get()
        self.telefone = self.entry_telefone.get()
        self.observacao = self.entry_observacao.get()
        self.horario = self.entry_hora.get()

        self.treeview.delete(*self.treeview.get_children())
        self.abrir_banco_de_dados_consultas()
        self.c.execute("""INSERT INTO consultas(nome_cliente, data_consulta, telefone, observacao, horario)
            VALUES(?, ?, ?, ?, ?);""", (self.nome, self.data_consulta, self.telefone, self.observacao, self.horario))
        self.conn.commit() ; print('Dados Inseridos')
        self.select_lista_consultas()
        self.desconectar_banco_de_dados_consultas()

