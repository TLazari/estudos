import threading
import time
import random

# Definindo o tamanho do buffer e os contadores
buffer_size = 5
buffer = []  # Usando uma lista simples para o buffer
contador_produtor = 100
contador_consumidor = 100
contador_buffer_vazio = 0
contador_buffer_cheio = 0
tempo = 0.2

# Função do produtor
def produtor():
    global contador_produtor, buffer, contador_buffer_cheio
    while contador_produtor > 0:
        # Introduzindo atraso no meio da verificação e manipulação
        if len(buffer) < buffer_size:
            item = random.randint(0, 100)
            buffer.append(item)
            print(f"Produzido: {item} | Contador: {contador_produtor} |Buffer atual: {buffer}")
            contador_produtor -= 1
        else:
            print("Buffer cheio")
            contador_buffer_cheio += 1
        #  controle de tempo aleatorio para desbalancear
        time.sleep(tempo)

# Função do consumidor
def consumidor():
    global buffer, contador_consumidor, contador_buffer_vazio
    while contador_consumidor > 0:
        # Introduzindo atraso no meio da verificação e manipulação
        if len(buffer) > 0:
            item = buffer.pop(0)
            print(f"Consumido: {item} | Contador: {contador_consumidor} |Buffer atual: {buffer}")
            contador_consumidor -= 1
        else:
            print("Buffer vazio")
            contador_buffer_vazio += 1
        #  controle de tempo aleatorio para desbalancear
        time.sleep(tempo)

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
print(f"\nTempo de execução: {tempo_execucao:.2f} segundos")
print(f"O buffer ficou vazio {contador_buffer_vazio} vezes e cheio {contador_buffer_cheio} vezes.")
