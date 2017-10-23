# ############ __slots__ for improved memory usage #############
# Overview:
# Custom types store their data in individualized, dynamic dictionaries
# via self.__dict__. Using __slots__ to limit available attribute names
# and move the name/key storage outside the instance to a type level
# can significantly improve memory usage. See EOF for perf numbers.


import collections
import datetime

ImmutableThingTuple = collections.namedtuple("ImmutableThingTuple", "a b c d")


class MutableThing:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class ImmutableThing:
    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


print("Uncomment just 1 of these 4 loops below")
print("after the program pauses on input, check the process memory")

count = 1000000
data = []

t0 = datetime.datetime.now()

# Loop 1: Tuples
# print("tuple")
# for n in range(count):
#     data.append((1 + n, 2 + n, 3 + n, 4 + n))

# # Loop 2: Named tuple
# print("named tuple")
# for n in range(count):
#     data.append(ImmutableThingTuple(1 + n, 2 + n, 3 + n, 4 + n))

# # Loop 3: Standard mutable class
# print("standard class")
# for n in range(count):
#     data.append(MutableThing(1 + n, 2 + n, 3 + n, 4 + n))

# # Loop 4: Slot based immutable class
print("slot based class")
for n in range(count):
    data.append(ImmutableThing(1 + n, 2 + n, 3 + n, 4 + n))

t1 = datetime.datetime.now()

input("Finished, waiting... done in {:,} s".format((t1 - t0).total_seconds()))

# Sample output on macOS + Python 3
# Hardware: Macbook Pro Early 2015 edition

# straight tuple:  43.2 MB, 0.556401 s
# named tuple:     42.6 MB, 1.514839 s
# standard class:  42.3 MB, 1.490941 s
# slot class:      40.6 MB, 1.421271 s

# Interesting real-world story of benefits of slots:
# http://tech.oyster.com/save-ram-with-python-slots/
