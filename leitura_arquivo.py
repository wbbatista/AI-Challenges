

def leitura_arquivo (arquivo_nome):
	
	with open(arquivo_nome) as arq:
		numero_sentencas = int(arq.readline())
		sentencas = arq.read().splitlines()

	return numero_sentencas, sentencas







