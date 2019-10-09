from leitura_arquivo import leitura_arquivo
from calculo_prefixo import calculo_prefixo



if __name__ == '__main__':

	# gerador de sentencas aleatorias 
	<FUNCAO GERADOR DE SENTENCAS>
	
	# leitura do arquivo
	numero_sentencas, sentencas = leitura_arquivo(<NOME ARQUIVO>)

	somas = []
	for sentenca in sentencas:

		# Soma da semelhanca de S com os seus sufixos 
		sem = <FUNCAO SOMA DE SEMELHANCA> (sentenca)
		# Guarda em array a soma das semelhancas
		somas.append(sem)		
		
	
	# impressao de saida
	for soma, sentenca in zip(somas,sentencas):
		print (sentenca,': ',int(soma))


	





