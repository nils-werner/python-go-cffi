from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source(
    'py._gosum',
    None,
    include_dirs=[],
    extra_compile_args=['-march=native', '-O3'],
    libraries=['fftw3', 'm'],
)

ffibuilder.cdef("""
typedef long long GoInt64;
typedef GoInt64 GoInt;
typedef double GoFloat64;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

GoInt Sum(GoInt p0, GoInt p1);
void Asin(GoSlice* p0, GoSlice* p1);
GoFloat64 Asum(GoSlice* p0);
GoSlice* ArrayToSlice(double* p0, GoInt p1);
""")

if __name__ == "__main__":
    ffibuilder.compile()
