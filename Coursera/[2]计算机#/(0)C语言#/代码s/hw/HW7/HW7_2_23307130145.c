#include <stdio.h>
void xs(int n)
{
	printf("1/%d=0.", n);
	int i = 0, j, x = 1, q[1000], r[1000], dec[1000], flag1 = 0, flag2 = 0;
	while (x != 0 && flag2 == 0)
	{
		++i;
		x *= 10;
		q[i] = dec[i] = x / n;
		r[i] = x = x % n;
		for (j = 1; j < i; j++)
		{
			if (q[j] == q[i] && r[j] == r[i])
			{
				flag1 = j;
				flag2 = i;
				break;
			}
		}
	}
	if (flag1)
	{
		for (i = 1; i < flag1; i++)
			printf("%d", dec[i]);
		printf("(");
		for (i = flag1; i < flag2; i++)
			printf("%d", dec[i]);
		printf(")\n");
	}
	else
	{
		for (j = 1; j <= i; j++)
			printf("%d", dec[j]);
		printf("\n");
	}
}
int main()
{
	int n;
    for (n = 2; n <= 100; n++)
    	xs(n);
	return 0;
}
