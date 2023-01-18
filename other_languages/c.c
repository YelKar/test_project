#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int fib(int n);
void delay(int number_of_seconds);

void main() {
    int a[5] = {1, 2, 3, 4, 5};
    a[6] = 7;
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("%d\n", a[6]);
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("%d\n", a[6]);
    fflush(stdout);
    delay(1);
    for (int i = 0; i < 12; i++) {
        printf("%d ", a[i]);
    }
    printf("%d\n", a[6]);
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("%d\n", a[6]);
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("%d\n", a[6]);
}

int fib(int n) {
    return n <= 2 ? 1 : fib(n - 1) + fib(n - 2);
}


void delay(int number_of_seconds) {
    int milli_seconds = 1000 * number_of_seconds;
    clock_t start_time = clock();
    while (clock() < start_time + milli_seconds);
}
