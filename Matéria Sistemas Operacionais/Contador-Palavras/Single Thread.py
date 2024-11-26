import time

# Tutorial (contagem de palavra)
# https://www.youtube.com/watch?v=GOa8VRJxGl8&ab_channel=Caf%C3%A9eComputa%C3%A7%C3%A3o


# Texto para contar palavras

texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularized in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum."""

# Função para contar palavras e separa-la em 3 partes
def separar_palavra(texto):
    parte1 = texto[:len(texto)//3] 
    parte2 = texto[len(texto)//3:2*len(texto)//3]
    parte3 = texto[2*len(texto)//3:]
    return parte1, parte2, parte3

# Função para contar caracteres
def contar_caracteres(parte):
    return len(parte)

# Início da medição do tempo

inicio_tempo = time.perf_counter()
resultado = separar_palavra(texto)
resultado_parte1 = contar_caracteres(resultado[0])
resultado_parte2 = contar_caracteres(resultado[1])
resultado_parte3 = contar_caracteres(resultado[2])
resultado_total = resultado_parte1 + resultado_parte2 + resultado_parte3
fim_tempo = time.perf_counter()

tempo_execucao = (fim_tempo - inicio_tempo) 
print(f"A frase possuí {resultado_total} caracteres, e o tempo de execução foi {(tempo_execucao)*1000000:.2f} microsegundos")

