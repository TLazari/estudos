import threading
import time
import random

# Definindo o tamanho do buffer e os contadores
buffer_size = 5
buffer = []
contador_produtor = 10
contador_consumidor = 10
contador_buffer_vazio = 0
contador_buffer_cheio = 0
tempo = 0.2

# Lock e condition para sincronização
lock = threading.Lock()
cond = threading.Condition(lock)

# Função do produtor
def produtor():
    global contador_produtor, contador_buffer_cheio, buffer
    while contador_produtor > 0:  # Continua enquanto houver itens para produzir
        with cond:
            while len(buffer) >= buffer_size:  # Espera enquanto o buffer estiver cheio
                print("Buffer cheio, produtor aguardando...")
                contador_buffer_cheio += 1
                cond.wait()
            # Produzindo item
            item = random.randint(0, 100)
            buffer.append(item)
            print(f"Produzido: {item} | Contador: {contador_produtor} | Buffer atual: {buffer}")
            contador_produtor -= 1
            cond.notify_all()  # Notifica que o buffer não está vazio
        time.sleep(tempo)

# Função do consumidor
def consumidor():
    global contador_consumidor, contador_buffer_vazio, buffer
    while contador_consumidor > 0:  # Continua enquanto houver itens para consumir
        with cond:
            while len(buffer) == 0:  # Espera enquanto o buffer estiver vazio
                print("Buffer vazio, consumidor aguardando...")
                contador_buffer_vazio += 1
                cond.wait()
            # Consumindo item
            item = buffer.pop(0)
            print(f"Consumido: {item} | Contador: {contador_consumidor} | Buffer atual: {buffer}")
            contador_consumidor -= 1
            cond.notify_all()  # Notifica que o buffer não está cheio
        time.sleep(tempo)

# Medindo o tempo de execução
inicio_tempo = time.time()

clear_prompt = print("\033[H\033[J", end='')

print ("Buffer com Thread Lock")


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
print(f"O buffer ficou vazio {contador_buffer_vazio} vezes e cheio {contador_buffer_cheio} vezes.")
