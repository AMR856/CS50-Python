#!/usr/bin/python3
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self.size + n > self._capacity:
            raise ValueError("Can't fill more than the jar capacity")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Can't remove from the negative size")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    print(jar.capacity)
    print(jar.size)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
