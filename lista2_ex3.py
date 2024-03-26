import threading
import random

# Criação de uma condição global
condition = threading.Condition()

# Função para gerar números aleatórios
def generate_numbers():
    with condition:
        for _ in range(10): # Gera 10 números aleatórios
            number = random.randint(1, 100)
            print(f"Número gerado: {number}")
            condition.notify() # Notifica a outra thread para escrever o número

# Função para escrever números em um arquivo
def write_numbers():
    with condition:
        with open("numbers.txt", "w") as file:
            for _ in range(10): # Espera por 10 números gerados
                condition.wait() # Espera pela notificação da outra thread
                number = random.randint(1, 100) # Simulação de leitura do número
                file.write(f"{number}\n")

# Criação das threads
thread_generate = threading.Thread(target=generate_numbers)
thread_write = threading.Thread(target=write_numbers)

# Início das threads
print("Threads Acordam")
thread_generate.start()
thread_write.start()

# Aguarda as threads terminarem
thread_generate.join()
thread_write.join()
print("Threads Param")