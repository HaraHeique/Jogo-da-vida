# -*- coding: utf-8 -*-
#Função que acha o X no mundo e armazena a sua posição dentro de uma lista

def achar_X(matriz_entrada) :
	lst_X = [];
	
	#Percorrendo toda a matriz na busca do X
	for x in range(len(matriz_entrada)) :      		#Quantidade de linhas da matriz de entrada
		for y in range(len(matriz_entrada[0])) :  	#Quantidade de colunas da matriz de entrada
			
			if (matriz_entrada[x][y] == "X") :
				
				lst_X.append((x,y));   #Lembrando que x é a linha e y a coluna
	
	return lst_X


#Função que acha o ponto(".") no mundo e armazena a sua posição em uma lista

def achar_ponto(matriz_entrada) :
	lst_ponto = [];
	
	#Percorrendo toda a matriz na busca de .
	for x in range(len(matriz_entrada)) :       	#Quantidade de linhas da matriz de entrada
		for y in range(len(matriz_entrada[0])) :  	#Quantidade de colunas da matriz de entrada
			
			if (matriz_entrada[x][y] == ".") :
				
				lst_ponto.append((x,y));   #Lembrando que x é a linha e y a coluna
	
	return lst_ponto
				
