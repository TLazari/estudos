import time
import threading

# Tutorial (multi thread)
# https://www.youtube.com/watch?v=dkptw_R7Qhc&ab_channel=ProfessorNetoPaschoal

# Texto para contar palavras
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularized in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum."""

def separar_palavra(texto):
    parte1 = texto[:len(texto)//3] 
    parte2 = texto[len(texto)//3:2*len(texto)//3]
    parte3 = texto[2*len(texto)//3:]
    return parte1, parte2, parte3

def contar_caracteres(parte, resultado, index):
    resultado[index] = len(parte)

# Início da medição do tempo
inicio_tempo = time.perf_counter()

resultado = separar_palavra(texto)
resultado_parte = [0, 0, 0]

# Criando threads
thread1 = threading.Thread(target=contar_caracteres, args=(resultado[0], resultado_parte, 0))
thread2 = threading.Thread(target=contar_caracteres, args=(resultado[1], resultado_parte, 1))
thread3 = threading.Thread(target=contar_caracteres, args=(resultado[2], resultado_parte, 2))

# Iniciando threads
thread1.start()
thread2.start()
thread3.start()

# Aguardando threads terminarem
thread1.join()
thread2.join()
thread3.join()

resultado_total = sum(resultado_parte)


fim_tempo = time.perf_counter()

tempo_execucao = (fim_tempo - inicio_tempo) 
print(f"A frase possuí {resultado_total} caracteres, e o tempo de execução foi {(tempo_execucao*1000000):.1f} microsegundos, ou seja, {(tempo_execucao*1000):.2f} milisegundos")