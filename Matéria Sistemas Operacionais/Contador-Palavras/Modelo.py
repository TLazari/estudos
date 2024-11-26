import threading
import time

# Texto para exemplo
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularized in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum."""

# Função para contar palavras
def contar_palavras(parte):
    return len(parte.split())

# Método sequencial para contar palavras
def contar_palavras_sequencial():
    # Dividindo o texto em três partes aproximadamente iguais
    partes = [texto[:len(texto)//3], texto[len(texto)//3:2*len(texto)//3], texto[2*len(texto)//3:]]
    
    total_palavras = 0
    for parte in partes:
        total_palavras += contar_palavras(parte)
    
    return total_palavras

# Método com threads para contar palavras
def contar_palavras_com_threads():
    # Dividindo o texto em três partes aproximadamente iguais
    partes = [texto[:len(texto)//3], texto[len(texto)//3:2*len(texto)//3], texto[2*len(texto)//3:]]
    
    # Lista para armazenar os resultados
    resultados = [0, 0, 0]
    
    # Função para thread contar as palavras
    def thread_contar_palavras(parte, indice):
        resultados[indice] = contar_palavras(parte)
    
    # Criar threads para contar palavras em cada parte
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_contar_palavras, args=(partes[i], i))
        threads.append(t)
        t.start()

    # Esperar todas as threads terminarem
    for t in threads:
        t.join()
    
    # Somar os resultados das partes
    return sum(resultados)
    
# Medir o tempo de execução para contagem sem threads
inicio_sequencial = time.perf_counter()
total_palavras_sequencial = contar_palavras_sequencial()
fim_sequencial = time.perf_counter()
tempo_sequencial = (fim_sequencial - inicio_sequencial) * 1_000_000  # Convertendo para microsegundos

# Medir o tempo de execução para contagem com threads
inicio_threads = time.time()
total_palavras_threads = contar_palavras_com_threads()
fim_threads = time.time()
tempo_threads = (fim_threads - inicio_threads) * 1_000_000 # Convertendo para microsegundos

# Exibir os resultados
print(f"Contagem de palavras (sequencial): {total_palavras_sequencial} palavras")
print(f"Tempo de execução (sequencial): {tempo_sequencial:.2f} microsegundos")

print(f"Contagem de palavras (com threads): {total_palavras_threads} palavras")
print(f"Tempo de execução (com threads): {tempo_threads:.2f} microsegundos")