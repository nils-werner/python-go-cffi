import contextlib
import numpy
import time
import math
from _sum import ffi


@contextlib.contextmanager
def time_print(task_name="", repititions=4):
    t = time.time()
    try:
        yield
    finally:
        print task_name, ":", time.time() - t, "s"


lib = ffi.dlopen("go/sum.so")

# Add two integers
lib.Sum(1, 2)


# Sin of NumPy array using Go
arr = numpy.arange(10000000, dtype=numpy.float64)

with time_print("Python"):
    out = numpy.zeros_like(arr)
    for v, i in enumerate(arr):
        out[i] = math.sin(v)

with time_print("Go"):
    out = numpy.zeros_like(arr)
    go_arr = lib.ArrayToSlice(
        ffi.cast("double*", arr.ctypes.data),
        len(arr)
    )
    go_out = lib.ArrayToSlice(
        ffi.cast("double*", out.ctypes.data),
        len(out)
    )
    lib.Asin(go_arr, go_out)

with time_print("NumPy"):
    numpy.sin(arr)


# Sum over NumPy array using Go
arr = numpy.random.rand(10000000).astype(numpy.float64)

with time_print("Python"):
    out = 0
    for i in arr:
        out += i

with time_print("Go"):
    go_arr = lib.ArrayToSlice(ffi.cast("double*", arr.ctypes.data), len(arr))
    lib.Asum(go_arr)

with time_print("NumPy"):
    numpy.sum(arr)
