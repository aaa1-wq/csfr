#include<stdio.h>
int a[31][31], sum, n;
void pri(int k)
{
	int i;
	for (i = k; i < n - k; i++)
		a[k][i] = ++sum;
	for (i = k + 1; i < n - k; i++)
		a[i][n - 1 - k] = ++sum;
	for (i = n - k - 2; i > k; i--)
		a[n - 1 - k][i] = ++sum;
	for (i = n - 1 - k; i > k; i--)
		a[i][k] = ++sum;
}
int main()
{
	printf("Enter n (0<n<=30): ");
	scanf("%d", &n);
	int i, j;
	for (i = 0; i <= n / 2; i++)
		pri(i);
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			printf("%4d", a[i][j]);
		printf("\n");
	}
	return  0;
}
