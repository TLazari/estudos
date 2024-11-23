import queue
import threading
import time
import random

# Definindo o tamanho do buffer e os contadores
buffer_size = 5
buffer = queue.Queue(buffer_size)
contador_produtor = 5
contador_consumidor = 5

# Função do produtor
def produtor():
    global contador_produtor
    while contador_produtor > 0:  # Continua enquanto houver itens para produzir
        if not buffer.full():  # Verifica se o buffer tem espaço
            item = random.randint(0, 100)
            buffer.put(item)
            print(f"Produzido: {item}")
            contador_produtor -= 1
        else:
            print("Buffer cheio")
        time.sleep(1)

# Função do consumidor
def consumidor():
    global contador_consumidor
    while contador_consumidor > 0:  # Continua enquanto houver itens para consumir
        if not buffer.empty():  # Verifica se o buffer não está vazio
            item = buffer.get()
            print(f"Consumido: {item}")
            contador_consumidor -= 1
        else:
            print("Buffer vazio")
        time.sleep(1)

# Medindo o tempo de execução
inicio_tempo = time.time()

# Criar threads para produtor e consumidor
thread_produtor = threading.Thread(target=produtor)
thread_consumidor = threading.Thread(target=consumidor)

# Iniciar threads
thread_produtor.start()
thread_consumidor.start()

# Esperar as threads terminarem
thread_produtor.join()
thread_consumidor.join()

fim_tempo = time.time()
tempo_execucao = fim_tempo - inicio_tempo

# Resultado final
print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
