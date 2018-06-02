# -*- coding: utf-8 -*-
#Função que serve para mostrar a matriz imprimida de forma correta, ou seja, sem os colchetes e afins

def mostrar_tela(mtz_entrada) :
	
	for x in range(len(mtz_entrada)) :       	#x vai corresponder a linha da matriz	
		
		
		for y in range(len(mtz_entrada[0])) :	#y corresponde a coluna da matriz
			print(mtz_entrada[x][y], end="");	#Imprimindo a matriz da forma como aparece no arquivo.txt
		
		print("\n", end="");		#Esse print serve para pular uma linha cada vez que ele imprimir a linha com os elementos da matriz
