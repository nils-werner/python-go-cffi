package main

import "C"
import "unsafe"
import "reflect"
import "fmt"

// Integer + Integer Summation
//export Sum
func Sum(a, b int) int {  
    return a + b
}

// Summation over double Array
//export Asum
func Asum(a *[]float64) (sum float64) {
    for _, v := range *a {
        sum += v
    }
    return
}

// Transform C double array to Go Slice
//export ArrayToSlice
func ArrayToSlice(a *C.double, length int) (*[]float64) {
    hdr := reflect.SliceHeader{
        Data: uintptr(unsafe.Pointer(a)),
        Len:  length,
        Cap:  length,
    }
    return (*[]float64)(unsafe.Pointer(&hdr))
}

func main() {
    a := []float64{1000.0, 2.0, 3.4, 7.0, 50.0}
    fmt.Printf("%+v\n", a)
    fmt.Printf("%+v\n", Asum(&a))
} 
