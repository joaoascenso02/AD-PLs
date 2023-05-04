from kazoo.client import KazooClient
from kazoo.recipe.barrier import DoubleBarrier
import time

# Criar um ZooKeeper handler
zh = KazooClient(hosts="localhost:2181")
zh.start()

# restante do programa
barrier = DoubleBarrier(zh, "/DUELO", 2)
print("Vou iniciar o jogo")

barrier.enter()
print("O jogo vai comecar")

while True:
    try:
        print("A jogar")
        time.sleep(1)

    except KeyboardInterrupt:
        break

print("Vou encerrar a minha participacao no jogo")
barrier.leave()
print("O jogo foi encerrado.\nA sua pontuacao foi X.")

zh.stop()
zh.close()
