class Subject:

    def __init__(self):
        self.observers = set()

    def add_observer(self, obs):
        self.observers.add(obs)

    def remove_observer(self, obs):
        self.observers.remove(obs)

    def notify(self, event):
        for obs in self.observers:
            obs(event)


def observer1(event):
    print("observer1 {}".format(event))


def observer2(event):
    print("observer2 {}".format(event))


if __name__ == "__main__":
    sub = Subject()
    sub.add_observer(observer1)
    sub.add_observer(observer2)
    sub.notify("A big event happened")

