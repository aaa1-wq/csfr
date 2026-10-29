#include "stdio.h"

int main(void)
{
    int i, j, n, temp, a[6][6];
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            a[i][j] = j + i * n;
    for (i = 0; i < n; i++)
        for (j = 0; j < n / 2; j++)
        {
            temp = a[n - j - 1][i];
            a[n - j - 1][i] = a[i][j];
            a[i][j] = temp;
        }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            printf("%d ", a[i][j]);
        printf("# ");
    }
    return 0;
}
