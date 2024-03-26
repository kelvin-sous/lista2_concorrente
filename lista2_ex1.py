import threading

# Função para imprimir números pares
def print_thread_1_num():
        for i in range(1, 6, 2):
            print(f"Nome: João, Número: {i}")

# Função para imprimir números ímpares
def print_thread_2_num():
        for i in range(2, 6, 2):
            print(f"Nome: Maria, Número: {i}")

# Criação das threads
thread_1 = threading.Thread(target=print_thread_1_num)
thread_2 = threading.Thread(target=print_thread_2_num)

# Início das threads
print("Thread 1 Acordou")
thread_1.start()
print("Thread 2 Acordou")
thread_2.start()

# Aguarda as threads terminarem
thread_1.join()
thread_2.join()