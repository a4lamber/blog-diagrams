'''
 # @ Author: Your name
 # @ Create Time: 2023-09-06 16:38:06
 # @ Modified by: Your name
 # @ Modified time: 2023-09-06 16:38:27
 # @ Description: old way of design the iterator
'''


import sys

class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current     