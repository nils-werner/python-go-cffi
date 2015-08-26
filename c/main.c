#include "../go/sum.h"
#include <stdio.h>

int main(int argc, char const *argv[])  
{
    // Add two ints
    printf("%lld\n", Sum(2, 40));

    // Sum over array of doubles
    double a[] = {1000.0, 2.0, 3.4, 7.0, 50.0};
    GoSlice *b = ArrayToSlice(a, 5);
    printf("%f\n", Asum(b));

    return 0;
}
