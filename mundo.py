# -*- coding: utf-8 -*-
def carrega_mundo(arquivo):
   with open(arquivo, "r") as arq:
      linhas = arq.readlines()

   matriz_mundo = []
   matriz = [[caractere for caractere in linha[:-1]] for linha in linhas]
   
   #Esse condicional serve para quando o arquivo(mundo) não for o arquivo 1, pois os outros arquivos está gerando sempre na última linha...
   #74 elementos e não 75
   if (arquivo != "entrada1.txt") :
	   matriz[len(matriz)-1].append(".");        

   return matriz
