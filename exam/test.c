#include "stdio.h"
#include "math.h"


int f(long n);

int main() {
    long start = pow(8, 10),
        stop;
    stop = start * 8;
    int c = 0;

    printf("start=%ld\nstop=%ld\n", start, stop);

    for (long i = start; i < stop; i++) {
        c += f(i);
//        if (i % 100000000 == 0) {
//            printf("%ld %ld\n", i, stop - i);
//        }
    }
    printf("%d\n", c);
}


int f(long n) {
    int prev = 0,
        c = 0,
        curr;

    while (n) {
        curr = (n % 8) % 2;
        c += curr;
        if ((prev == curr && curr == 1) || c > 3) {
            return 0;
        }
        prev = curr;
        n /= 8;
    }
    return c == 3;
}