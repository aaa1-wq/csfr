#include <stdio.h>
int main() {
    int a, b, c;
    if (scanf("%d %d %d", &a, &b, &c) != 3) return 1;

    printf("%.2f\n", (double)(a + b + c) / 3);
    return 0;
}