#include "stdio.h"


int _cfib(int n) {
    if (n < 2) {
        return 1;
    }
    return _cfib(n - 1) + _cfib(n - 2);
}