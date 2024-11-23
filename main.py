import queue
import threading
import time
import random

buffer_size = 5
buffer = []

def produtor():
    global buffer
    while True:
        if len(buffer) < buffer_size:
            item = random.randint(0, 100)
            buffer.append(item)
            print('Produzido:', item)
            time.sleep(1)
        if len(buffer) == buffer_size:
            print('Buffer cheio')
            break
    

def consumidor():
    global buffer
    while True:
        if len(buffer) > 0:
            item = buffer.pop(0)
            print('Consumido:', item)
            time.sleep(1)
        if len(buffer) == 0:
            print('Buffer vazio')
            break

inicio_tempo = time.time()
produtor()
consumidor()
fim_tempo = time.time()
tempo_execucao = fim_tempo - inicio_tempo
print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
