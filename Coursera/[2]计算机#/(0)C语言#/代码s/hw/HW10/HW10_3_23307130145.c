#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int main()
{
	srand(time(NULL));
	int n, i, x, a[105], m;
	printf("Enter n([1, 100]): ");
	scanf("%d", &n);
	printf("Randomly generate %d non negative integers within 100:\n", n);
	for (i = 0; i < n; i++)
	{
		x = rand() % 100;
		printf("%d ", x);
		a[i] = x;
	}
	printf("\nEnter m(<%d): ", n);
	scanf("%d", &m);
	printf("After moving:\n");
	for (i = 0; i < n; i++)
	{
		if (i < n - m)
			printf("%d ", *(a + m + i));
		else
			printf("%d ", *(a + i - n + m));
	}
	return 0;
}
