#include<stdio.h>
#include<math.h>

#define ONE_MIL 1000000

int partitions[ONE_MIL];

inline int get_partitions(int k) {
    if (k < 0) {
        return 0;
    }
    if (k >= ONE_MIL) {
        return -1;
    }
    return partitions[k];
}

inline int pos_mod(int i, int n) {
    return (i % n + n) % n;
}

int main() {
    partitions[0] = 1;
    int n = 1;
    int total, coeff, k, lb, ub;
    while (n < ONE_MIL) {
        //if (n%1000 == 0) printf("%d\n", n);
        total = 0;
        lb = (int)ceil(-(sqrt(24*n+1)+1.0)/6);
        ub = (int)floor((sqrt(24*n+1)-1.0)/6);
        //printf("%d <= k <= %d; ", lb, ub);
        for (k = lb; k <= ub; k++) {
            if (k == 0) continue;
            if (k % 2 == 0) coeff = -1;
            else coeff = 1;
            total += pos_mod(coeff*get_partitions(n - k*(3*k+1)/2), ONE_MIL);
            total = pos_mod(total, ONE_MIL);
        }
        //printf("p(%d) = %d\n", n, total);
        //total = total;
        if (total == 0) {
            printf("SOLUTION: %d\n", n);
            return 0;
        }
        partitions[n] = total;
        n++;
    }
}