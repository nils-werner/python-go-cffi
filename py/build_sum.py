from cffi import FFI

ffi = FFI()
ffi.set_source("py._sum", None)

ffi.cdef("""
typedef long long GoInt64;
typedef GoInt64 GoInt;

GoInt Sum(GoInt p0, GoInt p1);
""")

if __name__ == "__main__":
    ffi.compile()
