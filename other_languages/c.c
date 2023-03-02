#include "stdio.h"


long fib(int a);

int main (int argc, char *argv[]) {
    int n;
    sscanf(argv[1], "%d", &n);
    printf("%lu\n", fib(n));
    return 1;
}

long fib(int a) {
	if (a < 2) {
		return 1;
	}
	return fib(a-1) + fib(a-2);
}
