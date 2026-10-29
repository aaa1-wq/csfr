#include<stdio.h>
#include<math.h>
int main()
{
	double low = 0.0, high = 3.0, mid, f_low, f_high, f_mid = 1.0;
	printf("[low, high]             mid             f_low           f_high          f_mid\n");
	while (fabs(f_mid) > 1e-6)
	{
		mid = (low + high) / 2.0;
		f_low = low * low * low - low * low -1;
		f_high = high * high * high - high * high -1;
		f_mid = mid * mid * mid - mid * mid -1;
		printf("[%lf,%lf]\t%lf\t%lf\t%lf\t%lf\n", low, high, mid, f_low, f_high, f_mid);
		if (f_mid > 1e-6)
			high = mid;
		else
			low = mid;
	}
	printf("函数f(x)=x^3-x^2-1在区间[0,3]上的实根为%lf", mid);
	return 0;
}
