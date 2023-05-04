from kazoo.client import KazooClient
import time
import traceback


def critical_zone() -> None:
    print("Comecei a executar a zona critica")
    time.sleep(10)
    print("Terminei a zona critica")


def main() -> None:
    try:
        # Criar um ZooKeeper handler
        zh = KazooClient(hosts="localhost:2181")
        zh.start()

        # restante do programa
        zh.ensure_path("/LOCKS")
        zid = zh.create("/LOCKS/L-", ephemeral=True, sequence=True)
        print("Meu id: ", zid)

        while True:
            children = zh.get_children("/LOCKS")
            min_id = f"/LOCKS/{min(children)}"

            if zid == min_id:
                critical_zone()
                zh.delete(zid)
                break
            else:
                print("Children: ", children)
                time.sleep(1)

        zh.stop()
        zh.close()

    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
