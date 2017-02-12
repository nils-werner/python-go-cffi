Python to Go bindings using CFFI
================================

This project shows an example of how to interface with Go from Python using
CFFI (and not `#import <Python.h>`).

There are two main routines implemented in Go:

 - Add two integers
 - Sum over a Go Slice of float64s

Both functions are accessed from Go, C and Python. Additionally, Python is
actually passing a **NumPy array to Go**. The data is never copied but simply
cast to C and then wrapped in a Go Slice.

Compile and install:

    git clone https://github.com/nils-werner/python-go-cffi.git
    pip install -e python-go-cffi

Test:

    GODEBUG=cgocheck=0 python example.py


Currently, `GODEBUG=cgocheck=0` is required as we are passing C arrays to Go,
which is more strict in Go 1.6 and newer. Pull requests to fix this issue
are welcome!
