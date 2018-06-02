# -*- coding: utf-8 -*-
#Função para checar os vizinhos de "X" e caso necessário armazenar suas posições para serem mortos
#Morto quer dizer trocar "X" por "."

def vizinhos_X(lst_X, mtz_entrada) :
	lst_X_mortos = [];
	i = j = 0;
	cont_X = 0;
	
	for x in range(len(lst_X)) :    	#Fará o loop a quantidade de vezes que foi encontrado o "X"
		i = lst_X[x][0];            	#Recebe a linha que se encontra o "X" na tupla
		j = lst_X[x][1];				#Recebe a coluna que se encontra o "X" na tupla
		
		for l in range(i-1,i+2) :			#Percorrer da linha anterior ao "X" até a linha após ele
			
			if (l >= 0) and (l <= len(mtz_entrada)-1) :		#Restringe para a primeira linha (0) até a última linha (24)		
				
				for c in range(j-1,j+2) :	#Percorrer da coluna anterior ao "X" até a coluna após ele
					
					if (c >= 0) and (c <= len(mtz_entrada[0])-1) :    	#Restringe para a primeira coluna (0) até a última (74)
						
						if (mtz_entrada[l][c] == "X") :
							cont_X += 1;				#cont_X conta o número de vizinhos de "X" naquela dada posição
		
		cont_X -= 1;  #Realiza essa subtração pois no momento de checar os vizinhos checa também ele próprio, ou seja, o que não poderia
		if (cont_X != 2) and (cont_X != 3) :
			
			lst_X_mortos.append(lst_X[x]);  #Armazena a posição que se encontra o "X" que não possui 2 ou 3 vizinhos
		
		cont_X = 0; 					#Zerar o contador de vizinhos daquela dada posição onde se encontra o "X"
	
	#Retorna todas as posições dos "X" que deverão ser trocados por ".",ou seja, morrerão	
	return lst_X_mortos





#Função para checar os vizinhos dos pontos(".") e caso necessário armazenar suas posições para serem nascidos "X"

def vizinhos_ponto(lst_ponto, mtz_entrada) :
	lst_pontos_vivos = [];
	i = j = 0;
	cont_X = 0;
	
	for y in range(len(lst_ponto)) :    #Fará o loop da quantidade de vezes que foi achado o "."
		i = lst_ponto[y][0];			#Recebe a linha que se encontra o "." na tupla
		j = lst_ponto[y][1];			#Recebe a coluna que se encontra o "." na tupla
		
		for l in range(i-1,i+2) :			#Percorrer da linha anterior ao "." até a linha após ele
			
			if (l >= 0) and (l <= len(mtz_entrada)-1) :		#Restringe para a primeira linha (0) até a última linha (24)	
				
				for c in range(j-1,j+2) :	#Percorrer da coluna anterior ao "." até a coluna após ele
					
					if (c >= 0) and (c <= len(mtz_entrada[0])-1) :    	#Restringe para a primeira coluna (0) até a última (74)
						
						if (mtz_entrada[l][c] == "X") :
							cont_X += 1;				#cont_X conta o número de vizinhos de "." naquela dada posição
		
		if (cont_X == 3) :
			
			lst_pontos_vivos.append(lst_ponto[y])  #Armazena a posição que se encontra os "." onde possui exatamente 3 vizinhos
		
		cont_X = 0; 		#Zerar o contador do número de vizinhos que o "." naquela dada posição possui, pois será checado outro "."
		
	
	#Retorna todas as posições dos pontos(".") que deverão ser trocados por "X", pois irão nascer
	return lst_pontos_vivos
		
					
			
			
		
	
	
	
	
	
		
			
			
		
					
					 		
					
				
			
		
	
	

