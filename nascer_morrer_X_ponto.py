# -*- coding: utf-8 -*-
#Função que substitui nas posições necessárias o "X" por ".", ou seja, indicando que o organismo morreu...
#ou "." por "X", ou seja, indicando que um organismo nasceu

def substituicao_X_ponto(mtz_entrada, lst_X_mortos, lst_pontos_vivos) :
	l = c = 0;  
	
	for x in range(len(lst_X_mortos)) :	#loop para percorrer as posições que devem ser trocadas dos organismos que irão morrer
		
		l = lst_X_mortos[x][0];  #l vem de linha e pega a linha da posição que deve ser morta
		c = lst_X_mortos[x][1];	 #c vem de coluna e pega a coluna da posição que deve ser morta
		
		#A linha abaixo do código indica a atualização do mundo(mtz_entrada), onde substitui o organismo que estava vivo por morto
		mtz_entrada[l][c] = ".";   
	
	
	
	for y in range(len(lst_pontos_vivos)) : #loop para percorrer as posições que devem ser trocadas os organismos que irão nascer
		
		l = lst_pontos_vivos[y][0];  #l é a linha da posição que deve ser surgida(nascer)
		c = lst_pontos_vivos[y][1];  #c é a coluna da posição que deve ser surgida(nascer)
		
		#A linha abaixo indica a atualização do mundo(mtz_entrada), onde substitui o organismo que estava morto por vivo
		mtz_entrada[l][c] = "X";
	
	#A linha abaixo mostra o retorno da mtz_entrada(mundo) totalmente atualizada, ou seja, tanto dos organismos vivos quanto mortos
	return mtz_entrada
		
		
