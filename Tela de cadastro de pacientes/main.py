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
from relatorios import Relatorios
from tela_inicial import Tela_inicial


root = Tk()



class Application(Relatorios, Tela_inicial):
    def __init__(self):
        self.root = root
        self.gerar_tela_prinpipal()
        root.mainloop()

Application()