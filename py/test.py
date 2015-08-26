from _sum import ffi

lib = ffi.dlopen("go/sum.so")

print lib.Sum(1, 2)
