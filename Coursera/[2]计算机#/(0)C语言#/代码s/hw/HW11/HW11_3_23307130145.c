#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void exchange(int b[], int num)
{
	int *p = b, *q = b + num - 1, temp;
	while (p < q)
	{
		temp = *p;
		*p++ = *q;
		*q-- = temp;
	}
}
int main()
{
	srand(time(NULL));
	int n, a[105], i, x, m;
	printf("Enter n (<100): ");
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
	exchange(a, m);
	exchange(a + m, n - m);
	exchange(a, n);
	for (i = 0; i < n; i++)
		printf("%d ", a[i]);
}
