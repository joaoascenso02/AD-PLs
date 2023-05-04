from kazoo.client import KazooClient


zh = KazooClient(hosts="localhost:2181")
zh.start()

zh.ensure_path("/PAI")


@zh.DataWatch("/NORMAL")
def watch_node(data, stat):
    print(f"Stat: {stat}\nData: {data}")


@zh.ChildrenWatch("/PAI")
def watch_children(children):
    print(f"Children are now: {children}")


while True:
    pass


zh.stop()
zh.close()
