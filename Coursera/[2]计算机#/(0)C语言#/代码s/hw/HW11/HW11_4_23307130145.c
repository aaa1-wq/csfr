#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100

void create_array(int a[], int n)
{
	srand(time(NULL));
	int i;
	for (i = 0; i < n; i++)
		a[i] = rand() % 100;
}

void output_array(int a[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		printf("%4d", a[i]);
	printf("\n");
}

int copy_diff(int a[], int n, int b[])
{
	b[0] = a[0];
	int i, j, num = 1, flag = 0;
	for (i = 1; i < n; i++)
	{
		for (j = 0; j < i; j++)
			if (a[j] == a[i])
			{
				flag = 1;
				continue;
			}
		if (flag == 1)
		{
			flag = 0;
			continue;
		}
		b[num++] = a[i];
	}
	return num;
}

int main()
{
	int a[N], b[N], n;
	
	printf("Enter n(<=100): ");
	scanf("%d", &n);
	
	create_array(a, n);
	puts("The original array:");
	output_array(a, n);
	
	n = copy_diff(a, n, b);
	puts("The array copied without duplicate values:");
	output_array(b, n);
	
	return 0;
}
