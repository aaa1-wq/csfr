#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define nl printf("\n")
int main()
{
	srand(time(NULL));
	int x, i, maxn = -1, minn = 105, sum = 0, a[105], k;
	x = 1 + rand() % 100;
	for (i = 1; i <= x; i++)
	{
		k = rand() % 100;
		if (k > maxn)
			maxn = k;
		if (k < minn)
			minn = k;
		*(a + i) = k;
		sum += k;
	}
	printf("Random integer array (%d elements):\n", x);
	for (i = 1; i <= x; i++)
		printf("%d ", *(a + i));
	printf("\nMaximum integer: %d\n", maxn);
	printf("Minimum integer: %d\n", minn);
	printf("Average: %.1f", sum * 1.0 / x);
	return 0;
}
