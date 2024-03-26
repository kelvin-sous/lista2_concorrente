import threading
import time

# Função para imprimir números
def mensagem(Start):
    print(Start)
    time.sleep(5) # Espera 5 segundos antes de imprimir a próxima mensagem

# Criação da thread 1
thread = threading.Thread(target=mensagem, args=("Início Thread 1",))

# Início da thread
thread.start()

# Aguarda a thread terminar
thread.join()

# Criação da thread 2
thread = threading.Thread(target=mensagem, args=("Início Thread 2",))

# Início da thread
thread.start()

# Aguarda a thread terminar
thread.join()

# Criação da thread 3
thread = threading.Thread(target=mensagem, args=("Início Thread 3",))

# Início da thread
thread.start()

# Aguarda a thread terminar
thread.join()

# Criação da thread 4
thread = threading.Thread(target=mensagem, args=("Início Thread 4",))

# Início da thread
thread.start()

# Aguarda a thread terminar
thread.join()

# Criação da thread 5
thread = threading.Thread(target=mensagem, args=("Início Thread 5",))

# Início da thread
thread.start()

# Aguarda a thread terminar
thread.join()