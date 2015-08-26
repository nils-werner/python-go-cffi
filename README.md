Python to Go bindings using CFFI
================================

This project shows an example of how to interface with Go from Python using
CFFI (and not `#import <Python.h>`).

There are two main routines implemented in Go:

 - Add two integers
 - Sum over a Go Slice of float64s

Both functions are accessed from Go, C and Python. Additinally, Python is
actually passing a **NumPy array to Go**. The data is never copied but simply
cast to C and then wrapped in a Go Slice.

Compilation:

    virtualenv pygo
    cd pygo
    source bin/activate
    pip install -r requirements.txt
    make

Test:

    ./go/sum           # Test the Go part
    cd c && ./main     # Test the C part
    python py/test.py  # Test the Python part
