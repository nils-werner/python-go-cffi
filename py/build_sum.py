from cffi import FFI

ffi = FFI()
ffi.set_source("py._sum", None)

ffi.cdef("""
typedef long long GoInt64;
typedef GoInt64 GoInt;
typedef double GoFloat64;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

GoInt Sum(GoInt p0, GoInt p1);
GoFloat64 Asum(GoSlice* p0);
GoSlice* ArrayToSlice(double* p0, GoInt p1);
""")

if __name__ == "__main__":
    ffi.compile()
