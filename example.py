import contextlib
import numpy
import time
import math
from py import gosum


@contextlib.contextmanager
def time_print(task_name="", repititions=4):
    t = time.time()
    try:
        yield
    finally:
        print task_name, ":", time.time() - t, "s"


# Sin of NumPy array using Go
arr = numpy.arange(10000000, dtype=numpy.float64)

with time_print("Python"):
    out = numpy.zeros_like(arr)
    for i, v in enumerate(arr):
        out[i] = math.sin(v)

with time_print("Go"):
    gosum.Asin(arr)

with time_print("NumPy"):
    numpy.sin(arr)


# Sum over NumPy array using Go
arr = numpy.random.rand(10000000).astype(numpy.float64)

with time_print("Python"):
    out = 0
    for i in arr:
        out += i

with time_print("Go"):
    gosum.Asum(arr)

with time_print("NumPy"):
    numpy.sum(arr)
