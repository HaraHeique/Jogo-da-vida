# -*- coding: utf-8 -*-
#Arquivo para teste de matrizes de tamanhos diferentes. Lembrando se trocar de uma matriz...
#diferente do tamanho mundo(25x75) tem que modificar alguns arquivos do programa.

#Chamando funções
from achar_X_ponto import achar_X, achar_ponto;
from vizinhos_X_ponto import vizinhos_X, vizinhos_ponto;
from nascer_morrer_X_ponto import substituicao_X_ponto;
from impressao_tela import mostrar_tela;
from mundo import carrega_mundo;

import os;
import time;




def main():
	
	mtz_entrada = carrega_mundo("entrada6.txt");
	
	for x in range(len(mtz_entrada)) :
		print(len(mtz_entrada));
	
	
	#Número de interações que o usuário deseja
	n = int(input("Insira o número de interacoes desejadas: "));
	
	
	for _ in range(n) :
		#Colocar em uma lista todas as posições de "X" e "." para poder fazer as trocas segundo as condições dadas
		lst_X = achar_X(mtz_entrada);
		lst_ponto = achar_ponto(mtz_entrada);
		
	
	
		#Checar e armazenar em uma lista os vizinhos de "X" e ".", e concluir quem é necessário morrer ou viver segundo as condições 
		lst_X_mortos = vizinhos_X(lst_X, mtz_entrada);
		lst_pontos_vivos = vizinhos_ponto(lst_ponto, mtz_entrada);
	
	
		#Substituir o "X" por "." e/ou substituir o "." por "X" segundo as condições dadas no jogo
		#Logo depois imprimir o mundo(matriz) atualizada
		mtz_entrada = substituicao_X_ponto(mtz_entrada, lst_X_mortos, lst_pontos_vivos);
		
		
		#Imprimindo cada linha do mundo atualizado
		print("LOADING...");
		
		time.sleep(5); 				   #Espera um tempo de 5 segundo como se fosse carregando a atualização do mundo novo
		os.system("cls");			   #Limpando tela
		
		mostrar_tela(mtz_entrada);     #Mostrando a atualização do mundo
		time.sleep(10);				   #Mostrando o mundo por 10 segundos
		os.system("cls");			   #Limpando a tela
		
	return 0

if __name__ == '__main__':
	main()

