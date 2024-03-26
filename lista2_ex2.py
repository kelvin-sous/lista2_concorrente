import threading

# Variável global que será incrementada pelas threads
global_variable = 0
# Lock para sincronização
lock = threading.Lock()

# Função para incrementar a variável global
def increment_global():
    global global_variable
    for _ in range(100):
        # Adquire o lock antes de modificar a variável global
        lock.acquire()
        global_variable += 1
        # Libera o lock após a modificação
        lock.release()

# Lista para armazenar as threads
threads = []

# Cria e inicia as threads
for _ in range(10):
    t = threading.Thread(target=increment_global)
    t.start()
    threads.append(t)

# Espera todas as threads terminarem
for t in threads:
    t.join()

# Mostra o valor final da variável global
print("Valor final da variável global:", global_variable)
