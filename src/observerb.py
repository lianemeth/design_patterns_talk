class Subject:    
    observers = set()

    @classmethod
    def observer(cls, obs):
        cls.observers.add(obs)
        return obs

    def notify(self, event):
        for obs in self.observers:
            obs(event)

@Subject.observer
def observer1(event):
    print("observer1 {}".format(event))

@Subject.observer
def observer2(event):
    print("observer2 {}".format(event))

if __name__ == "__main__":
    sub = Subject()
    sub.notify("A big event happened")

