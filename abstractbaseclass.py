from abc import ABC, abstractmethod


class Computer:
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running")


class Programmer:
    def work(self, com):
        print('its debugging')


com = Programmer()
com.work()



