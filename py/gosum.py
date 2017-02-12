from __future__ import absolute_import

import os
import numpy
from ._gosum import ffi

here = os.path.dirname(os.path.abspath(__file__))
lib = ffi.dlopen(os.path.join(here, "__gosum.so"))


def Sum(p0, p1):
    return lib.Sum(p0, p1)


def Asin(indata, outdata=None):
    if outdata is None:
        outdata = numpy.zeros_like(indata)

    go_input = lib.ArrayToSlice(
        ffi.cast("double*", indata.ctypes.data),
        len(indata)
    )
    go_output = lib.ArrayToSlice(
        ffi.cast("double*", outdata.ctypes.data),
        len(outdata)
    )

    lib.Asin(go_input, go_output)
    return outdata


def Asum(indata):
    go_indata = lib.ArrayToSlice(ffi.cast("double*", indata.ctypes.data), len(indata))
    return lib.Asum(go_indata)
