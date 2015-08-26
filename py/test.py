import numpy
from _sum import ffi

lib = ffi.dlopen("go/sum.so")

# Add two integers
print lib.Sum(1, 2)


# Sum over NumPy array using Go
arr = numpy.array([1000.0, 2.0, 3.4, 7.0, 50.0], dtype=numpy.float64)
go_arr = lib.ArrayToSlice(ffi.cast("double*", arr.ctypes.data), len(arr))

print lib.Asum(go_arr)
