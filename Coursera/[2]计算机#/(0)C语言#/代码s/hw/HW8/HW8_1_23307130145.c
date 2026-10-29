#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define maxn 101
#define nl printf("\n")
int n, a[maxn];
void gen()
{
	int i;
	printf("Randomly generate %d positive integers (<100):\n", n);
	for (i = 0; i < n; i++)
	{
		a[i] = rand() % 100;
		printf("%d ", a[i]);
	}
	nl;
}
void sorting()
{
	printf("After sorting:\n");
	int end, pos, j, i, sum1 = 1, sum2 = 1;
	end = n - 1;
	while(end)
	{
		for (j = pos = 0; j < end; j++)
			if (a[j] > a[j + 1])
			{
				int temp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = temp;
				pos = j;	
			}
		end = pos;
	}
	printf("%d ", a[0]);
	for (i = 1; i < n; i++)
	{
		printf("%d ", a[i]);
		if (a[i] == a[i - 1])
			sum1++;
		else
		{
			if (sum1 > sum2)
				sum2 = sum1;
			sum1 = 1;
		}
	}
	nl;
	printf("The length of the longest platform: %d", sum2);
}
int main()
{
	srand((unsigned int)time(NULL));
	printf("Enter a positive integer n (n<=100): ");
	scanf("%d", &n);
	gen();
	sorting();
	return 0;
}
