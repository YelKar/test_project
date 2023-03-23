#include <stdio.h>

int r(int n);
int is_odd(int n);
void task5();

int main() {
    task5();
    return 0;
}

void task5() {
    int start = 123456789,
        stop = 1987654321,
        count = 0,
        res, n;

    for (n = 15000000; (res = r(n)) <= stop; n++) {
        count += res >= start;
        if (n % 10000000 == 0) {
            printf("N=%d\tR=%d\n", n, res);
        }
    }
    printf("\nN=%d => R=%d\nresult=%d\n", n, r(n), count);
}

int r(int n) {
    n = (n * 2) + is_odd(n);
    n = (n * 2) + is_odd(n);
    n = (n * 2) + is_odd(n);
    return n;
}

int is_odd(int n) {
    int s = 0;
    while (n) {
        s += n % 10;
        n /= 10;
    }
    return s % 2;
}