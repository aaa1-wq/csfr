#include<stdio.h>
int main()
{
	double x, a = 1.0, ans = 1.0;
	int i = 1, flag = 0;
	printf("Enter x: ");
	scanf("%lf", &x);
	if (x < 0)
	{
		flag = 1;
		x *= -1.0;
	}
	while (a > 1e-10)
	{
		a = a * x / (i * 1.0);
		if (a > 1e-10) 
			ans += a;
		i++;
	}
	printf("e^(%lg) = %.15lg", x, flag > 0 ? 1.0 / ans : ans);
	return 0;
}
