from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import urllib
import datetime
from funçoes import *


#variaveis
tabela_pacientes = pd.read_excel(r'.\HorarioPacientes.xlsx')
dataSeguinte = str(datetime.date.today() + datetime.timedelta(days=1))
navegador = webdriver.Chrome(executable_path='./chromedriver')

now = datetime.datetime.now()

#abrindo o navegador
navegador.get("https://web.whatsapp.com/")
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

    #descobrindo para quem mandar mensagem
for linha,valor in enumerate(tabela_pacientes['Data']):
    if compararString(dataSeguinte,f'{valor}'[0:10]) == True:
        hora = f'{tabela_pacientes["Horario"][linha]}'[:5]
        if  6 <=  int(now.hour) < 12:
            texto = urllib.parse.quote(f'Bom dia {tabela_pacientes["Nome"][linha].capitalize()}, tudo bem? confirmando sua consulta amanhã as {hora}')
        elif 12 <=  int(now.hour) < 18:
            texto = urllib.parse.quote(f'Bom tarde {tabela_pacientes["Nome"][linha].capitalize()}, tudo bem? confirmando sua consulta amanhã as {hora}')
        elif 18 <=  int(now.hour) < 23:
            texto = urllib.parse.quote(f'Boa noite {tabela_pacientes["Nome"][linha].capitalize()}, tudo bem? confirmando sua consulta amanhã as {hora}')
        numero = f"55{tabela_pacientes['Telefone'][linha]}"
        numero2 = numero[0:13]


        link = f"https://web.whatsapp.com/send?phone={numero2}&text={texto}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(7)
print('ACABOU')



