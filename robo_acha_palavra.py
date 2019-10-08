from pathlib import Path, PureWindowsPath
import PyPDF2
import re
import os

#Script simples para abrir, percorres e encotrar termos em arquivos pdf

#Atribui as palavras chaves a serem procuradas
palavra_chave_1 = "termo"
palavra_chave_2 = "termo"
palavra_chave_3 = "termo"
palavra_chave_4 = "termo"

palavra_chave_5 = "termo"
palavra_chave_6 = "termo"
palavra_chave_7 = "termo"
palavra_chave_8 = "termo"

palavra_chave_9 = "termo"
palavra_chave_10 = "termo"
palavra_chave_11 = "termo"
palavra_chave_12 = "termo"

palavra_chave_13 = "termo"
palavra_chave_14 = "termo"
palavra_chave_15 = "termo"
palavra_chave_16 = "termo"


Fonte = Path(r"C:\documentos\pasta")

#Função principal -> se tiver paciência crie funções para somas e porcentagens
def procura_palavra():  
    #Lista os arquivos na pasta
    Caminho = os.listdir(Fonte)
    #Percorre as pastas
    for caminho in Caminho:
        #Abre cada um arquivo
        Fonte2 = os.path.join(Fonte, caminho)
        fonte = open(Fonte2, "rb")
        pdf = PyPDF2.PdfFileReader(fonte)
        num_pagina = pdf.getNumPages()

        #Valores inteiros a serem atribuidos depois do "for"
        soma_total = 0
        soma_palavra_chave_1 = 0
        soma_palavra_chave_2 = 0
        soma_palavra_chave_3 = 0
        soma_palavra_chave_4 = 0
        soma_palavra_chave_5 = 0
        soma_palavra_chave_6 = 0
        soma_palavra_chave_7 = 0
        soma_palavra_chave_8 = 0
        soma_palavra_chave_9 = 0
        soma_palavra_chave_10 = 0
        soma_palavra_chave_11 = 0
        soma_palavra_chave_12 = 0
        soma_palavra_chave_13 = 0
        soma_palavra_chave_14 = 0
        soma_palavra_chave_15 = 0
        soma_palavra_chave_16 = 0
        
        #Laço que percorre cada pagina do arquivo
        for pagina in range(num_pagina):
            numero_da_pagina = pdf.getPage(pagina)
            #Captura o conteudo da pagina
            conteudo_da_pagina = numero_da_pagina.extractText()

            #Ajusta o conteudo capturado, neste caso foi atribuido apenas o .lower()
            conteudo_ajustado = conteudo_da_pagina.lower()

            #Recebe o tamanho do conteudo 
            conteudo_geral = len(conteudo_ajustado)

            #Procura em cada pagina a palavra chave selecionada -> prática ruim, no futuro transforme em uma função
            palavra_chave_1_encontrada = len(re.findall(palavra_chave_1, conteudo_ajustado))
            palavra_chave_2_encontrada = len(re.findall(palavra_chave_2, conteudo_ajustado))
            palavra_chave_3_encontrada = len(re.findall(palavra_chave_3, conteudo_ajustado))
            palavra_chave_4_encontrada = len(re.findall(palavra_chave_4, conteudo_ajustado))
            palavra_chave_5_encontrada = len(re.findall(palavra_chave_5, conteudo_ajustado))
            palavra_chave_6_encontrada = len(re.findall(palavra_chave_6, conteudo_ajustado))
            palavra_chave_7_encontrada = len(re.findall(palavra_chave_7, conteudo_ajustado))
            palavra_chave_8_encontrada = len(re.findall(palavra_chave_8, conteudo_ajustado))
            palavra_chave_9_encontrada = len(re.findall(palavra_chave_9, conteudo_ajustado))
            palavra_chave_10_encontrada = len(re.findall(palavra_chave_10, conteudo_ajustado))
            palavra_chave_11_encontrada = len(re.findall(palavra_chave_11, conteudo_ajustado))
            palavra_chave_12_encontrada = len(re.findall(palavra_chave_12, conteudo_ajustado))
            palavra_chave_13_encontrada = len(re.findall(palavra_chave_13, conteudo_ajustado))
            palavra_chave_14_encontrada = len(re.findall(palavra_chave_14, conteudo_ajustado))
            palavra_chave_15_encontrada = len(re.findall(palavra_chave_15, conteudo_ajustado))
            palavra_chave_16_encontrada = len(re.findall(palavra_chave_16, conteudo_ajustado))
            
            #Adiciona o numero de palavras chaves ao valor inteiro anterior -> no futuro transforme em uma função
            soma_palavra_chave_1 += palavra_chave_1_encontrada
            soma_palavra_chave_2 += palavra_chave_2_encontrada
            soma_palavra_chave_3 += palavra_chave_3_encontrada
            soma_palavra_chave_4 += palavra_chave_4_encontrada
            soma_palavra_chave_5 += palavra_chave_5_encontrada
            soma_palavra_chave_6 += palavra_chave_6_encontrada
            soma_palavra_chave_7 += palavra_chave_7_encontrada
            soma_palavra_chave_8 += palavra_chave_8_encontrada
            soma_palavra_chave_9 += palavra_chave_9_encontrada
            soma_palavra_chave_10 += palavra_chave_10_encontrada
            soma_palavra_chave_11 += palavra_chave_11_encontrada
            soma_palavra_chave_12 += palavra_chave_12_encontrada
            soma_palavra_chave_13 += palavra_chave_13_encontrada
            soma_palavra_chave_14 += palavra_chave_14_encontrada
            soma_palavra_chave_15 += palavra_chave_15_encontrada
            soma_palavra_chave_16 += palavra_chave_16_encontrada

            #Adiciona o valor total de todas as paginas ao valor inteiro anterior
            soma_total += conteudo_geral
            
            #Calcula o valor percentual de cada elemento encontrado em relação ao total
            percentual_palavra_chave_1 = soma_palavra_chave_1 * 100/soma_total
            percentual_palavra_chave_2 = soma_palavra_chave_2 * 100/soma_total
            percentual_palavra_chave_3 = soma_palavra_chave_3 * 100/soma_total
            percentual_palavra_chave_4 = soma_palavra_chave_4 * 100/soma_total
            percentual_palavra_chave_5 = soma_palavra_chave_5 * 100/soma_total
            percentual_palavra_chave_6 = soma_palavra_chave_6 * 100/soma_total
            percentual_palavra_chave_7 = soma_palavra_chave_7 * 100/soma_total
            percentual_palavra_chave_8 = soma_palavra_chave_8 * 100/soma_total
            percentual_palavra_chave_9 = soma_palavra_chave_9 * 100/soma_total
            percentual_palavra_chave_10 = soma_palavra_chave_10 * 100/soma_total
            percentual_palavra_chave_11 = soma_palavra_chave_11 * 100/soma_total
            percentual_palavra_chave_12 = soma_palavra_chave_12 * 100/soma_total
            percentual_palavra_chave_13 = soma_palavra_chave_13 * 100/soma_total
            percentual_palavra_chave_14 = soma_palavra_chave_14 * 100/soma_total
            percentual_palavra_chave_15 = soma_palavra_chave_15 * 100/soma_total
            percentual_palavra_chave_16 = soma_palavra_chave_16 * 100/soma_total
            
            #Caso queira junte os termos em proxies
            soma_proxy_1 = (soma_palavra_chave_1 + soma_palavra_chave_2 + soma_palavra_chave_3 + soma_palavra_chave_4)
            soma_proxy_2 = (soma_palavra_chave_5 + soma_palavra_chave_6 + soma_palavra_chave_7 + soma_palavra_chave_8)
            soma_proxy_3 = (soma_palavra_chave_9 + soma_palavra_chave_10 + soma_palavra_chave_11 + soma_palavra_chave_12)
            soma_proxy_4 = (soma_palavra_chave_13 + soma_palavra_chave_14 + soma_palavra_chave_15 + soma_palavra_chave_16)


        
        #Retorna na tela os valores encontrados
        print(">>> {} foi citado".format(palavra_chave_1), soma_palavra_chave_1, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_1)
        print(">>> {} foi citado".format(palavra_chave_2), soma_palavra_chave_2, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_2)
        print(">>> {} foi citado".format(palavra_chave_3), soma_palavra_chave_3, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_3)
        print(">>> {} foi citado".format(palavra_chave_4), soma_palavra_chave_4, " de ", soma_total, "resultado: ",)# percentual_palavra_chave_4)
        print(">>> {} soma da proxy blockchain".format(soma_proxy_1))
        print(">>> {} foi citado".format(palavra_chave_5), soma_palavra_chave_5, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_5)
        print(">>> {} foi citado".format(palavra_chave_6), soma_palavra_chave_6, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_6)
        print(">>> {} foi citado".format(palavra_chave_7), soma_palavra_chave_7, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_7) 
        print(">>> {} foi citado".format(palavra_chave_8), soma_palavra_chave_8, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_8)
        print(">>> {} soma da proxy bitcoin".format(soma_proxy_2))
        print(">>> {} foi citado".format(palavra_chave_9), soma_palavra_chave_9, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_9)
        print(">>> {} foi citado".format(palavra_chave_10), soma_palavra_chave_10, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_10)
        print(">>> {} foi citado".format(palavra_chave_11), soma_palavra_chave_11, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_11)
        print(">>> {} foi citado".format(palavra_chave_12), soma_palavra_chave_12, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_12)
        print(">>> {} soma da proxy inovacao".format(soma_proxy_3))
        print(">>> {} foi citado".format(palavra_chave_13), soma_palavra_chave_13, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_13)
        print(">>> {} foi citado".format(palavra_chave_14), soma_palavra_chave_14, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_14)
        print(">>> {} foi citado".format(palavra_chave_15), soma_palavra_chave_15, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_15)
        print(">>> {} foi citado".format(palavra_chave_16), soma_palavra_chave_16, " de ", soma_total, "resultado: ",) #percentual_palavra_chave_16)
        print(">>> {} soma da proxy fintech".format(soma_proxy_4))
        print("-----------------------------------------------------------------------------------------------------------")

        
procura_palavra()