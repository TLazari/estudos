import threading
import time
import os

def soma():
    resultado = int(valor1) + int(valor2)
    print("Soma: ", resultado)

def subtracao():
    resultado = int(valor1) - int(valor2)
    print("Subtração: ", resultado)

def multiplicacao():
    resultado = int(valor1) * int(valor2)
    print("Multiplicação: ", resultado)

def divisao():
    resultado = int(valor1) / int(valor2)
    print("Divisão: ", resultado)

clear_prompt = print("\033[H\033[J", end='')

print ("Calculadora Multithread")

valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

thread1 = threading.Thread(target=soma)
thread2 = threading.Thread(target=subtracao)
thread3 = threading.Thread(target=multiplicacao)
thread4 = threading.Thread(target=divisao)

inicio = time.perf_counter()
threads = [thread1, thread2, thread3, thread4]

for thread in threads:
    thread.start()
    thread.join()

fim_tempo = time.perf_counter()
tempo_execucao = (fim_tempo - inicio) * 1_000

print(f"Tempo de execução: {(tempo_execucao):.2f} milissegundos")
print("Fim da execução")
