# -*- coding: utf-8 -*-

def main():
	#Declarando variáveis
	n = 0;  #Indica o número de vezes que será as interações
	arquivo_n = 0;  #Indica o número do arquivo de entrada que o usuário desejar
	mtz_entrada = None;  #Indica qual mundo de entrada será usado
	
	#Chamadas de funções
	from trava_entrada import trava_arquivo_n, trava_interacao;
	from mundo import carrega_mundo;
	from impressao_tela import mostrar_tela;
	from achar_X_ponto import achar_X, achar_ponto;
	from vizinhos_X_ponto import vizinhos_X, vizinhos_ponto;
	from nascer_morrer_X_ponto import substituicao_X_ponto;
	
	import time;
	import os;
	
	
	#Begin
	print("JOGO DA VIDA\n\n");
	print("Você pode escolher arquivos de entrada de 1 a 5 que representa o mundo.");
	
	arquivo_n = int(input("Insira o mundo que deseja: "));
	
	os.system("cls");  #Limpar tela
	
	#Caso o usuário digite um valor de entrada diferente de 1 a 5 chama uma função que funciona como trava
	if (arquivo_n < 1) or (arquivo_n > 6) :
		arquivo_n = trava_arquivo_n(arquivo_n);
	

	n = int(input("Número de interacoes que deseja no mundo escolhido: "));
	
	os.system("cls");  #Limpar tela
	
	#Caso o usuário digite um valor de interações abaixo de 0 chama uma função que trava isso
	if (n < 0) :
		n = trava_interacao(n);
	
	
	#Transformando o número do arquivo em string para poder chamar a função mundo
	arquivo_n = "entrada" + str(arquivo_n) + ".txt";    
	
	#Chamando o mundo a partir da função carrega_mundo
	mtz_entrada = carrega_mundo(arquivo_n);
	
	#Chamando a função para mostrar a impressão da matriz(mundo) escolhido pelo usuário
	print("O mundo escolhido foi esse abaixo: \n\n");
	mostrar_tela(mtz_entrada);
	
	time.sleep(10);	   	#Tempo de 10 segundos para o usário checar o mundo que ele escolheu
	os.system("cls");  	#Limpar tela
	
	
	#Loop do número de interações desejadas pelo usuário
	
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
		
		time.sleep(2); 				   #Espera um tempo de 2 segundos como se fosse carregando a atualização do mundo novo
		os.system("cls");			   #Limpando tela
		
		mostrar_tela(mtz_entrada);     #Mostrando a atualização do mundo
		time.sleep(3);				   #Mostrando o mundo por 3 segundos
		os.system("cls");			   #Limpando a tela
		
	
	print("Obrigado por usar!");
	
	#End
		

	return 0

if __name__ == '__main__':
	main()

