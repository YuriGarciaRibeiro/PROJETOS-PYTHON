from ast import Str
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



class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf')

    def geraRelatorioCliente(self):
        
        # Cria o arquivo PDF
        self.c = canvas.Canvas("cliente.pdf")

        # recebendo os dados do cliente
        self.codRel = self.entry_codigo.get()
        self.nomeRel = self.entry_nome.get()
        self.telefoneRel = self.entry_telefone.get()
        self.sexoRel = self.entry_sexo.get()
        self.estado_civilRel = self.entry_estado_civil.get()
        self.data_nascimentoRel = self.entry_data_nascimento.get()

        # Criando o cabeçalho
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 750, "Ficha do Cliente")

        # Criando o corpo do relatório
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(50, 700, "Código: " )
        self.c.drawString(50, 680, "Nome: " )
        self.c.drawString(50, 660, "Data de Nascimento: " )
        self.c.drawString(50, 640, "Telefone: " )
        self.c.drawString(50, 620, "Sexo: " )
        self.c.drawString(50, 600, "Estado Civil: " )

        self.c.setFont("Helvetica", 12)
        self.c.drawString(150, 700, self.codRel)
        self.c.drawString(150, 680, self.nomeRel)
        self.c.drawString(180, 660,  self.data_nascimentoRel)
        self.c.drawString(150, 640,  self.telefoneRel)
        self.c.drawString(150, 620,  self.sexoRel)
        self.c.drawString(150, 600,  self.estado_civilRel)


        self.c.rect(20,10,550,820, fill=False, stroke=True)
        
        self.c.showPage()
        self.c.save()
        self.printCliente()