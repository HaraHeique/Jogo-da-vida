# -*- coding: utf-8 -*-
#Função que serve como trava caso o usuário digite um valor acima de 5 e abaixo de 1

import os;

def trava_arquivo_n(arquivo_n) :
	while (arquivo_n < 1) or (arquivo_n > 5) :
		print("Você digitou um valor abaixo 1 ou acima 5.\nPor favor digite novamente abaixo:");
		arquivo_n = int(input());
		
		os.system("cls");  #Limpar tela
	
	return arquivo_n       #Sempre vai retornar valores de 1 a 5



#Função para trava de interações negativas inseridas pela usuário

def trava_interacao(n) :
	while (n < 0) :
		print("Você digitou um número de interacoes abaixo de 0.\nPor favor digite novamente abaixo:");
		n = int(input());
	
		os.system("cls");  #Limpar tela
	
	return n			   #Sempre vai retornar valores positivos ou 0
	 
	
