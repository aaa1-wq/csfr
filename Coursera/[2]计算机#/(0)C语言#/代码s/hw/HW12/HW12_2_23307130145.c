#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
	srand(time(NULL));
	int a[10], range, *p[15], i, j, b[10], num = 1;
	printf("Enter the range: ");
	scanf("%d", &range);
	printf("Randomly generate 10 positive interers within %d:\n", range);
	for (i = 0; i < 10; i++)
	{
		a[i] = rand() % range;
		printf("%4d", a[i]);
		p[i] = &a[i];
	}
	printf("\n");
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10 - i; j++)
		{
			if (*p[j] > *p[j + 1])
			{
				int *temp = p[j];
				p[j] = p[j + 1];
				p[j + 1] = temp;
			}
		}
	}
	*(p[0] - a + b) = 1;
	for (i = 1; i < 10; i++)
		*(p[i] - a + b) = (*p[i] == *p[i - 1]) ? num : ++num;
	printf("Their sequence numbers in ascending order:\n");
	for (i = 0; i < 10; i++)
		printf("%4d", b[i]);
	return 0;
}
