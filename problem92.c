#include<stdio.h>

int next(int n) {
    int total = 0;
    for( ; n > 0; n /= 10) {
        int d = n % 10;
        total += d*d;
    }
    return total;
}

int main() {
    int k, n, count;
    count = 0;
    for (n = 1; n < 10000000; n++) {
        k = n;
        while (k != 1 && k != 89)
            k = next(k);
        if (k == 89) count++;
    }
    printf("%d", count);
    return -1;
}