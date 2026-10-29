#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define nl printf("\n")
int a[105][105];
int main()
{
	srand(time(NULL));
	int n, i, j, k;
	printf("Enter the order of a square matrix([1, 100]): ");
	scanf("%d", &n);
	printf("Randomly generate an %d-order square matrix within 100:\n", n);
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			a[i][j] = rand() % 100;
			printf("%4d", a[i][j]);
		}
		nl;
	}		
	for (k = 0; k < ((n % 2) ? n : n + 1) / 2; k++)
	{
		int first = k, last = n - 1 - k;
		for (i = first; i < last; i++)
		{
			int temp = a[first][i], offset = n - 1 - i;
			a[first][i] = a[i][last];
			a[i][last] = a[last][offset];
			a[last][offset] = a[offset][first];
			a[offset][first] = temp;
		}
	}
	printf("The square matrix after 90 degrees counterclockwise rotation:\n");
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			printf("%4d", a[i][j]);
		nl;
	}
	return 0;
}
