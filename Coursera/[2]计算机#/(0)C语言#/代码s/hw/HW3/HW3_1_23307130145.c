#include<stdio.h>
int main()
{
	int sum1 = 0, sum2 = 0, a, flag;
	printf("Enter a 13-digit EAN: ");
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	sum2 += a;
	a = getchar() - '0';
	sum1 += a;
	a = getchar() - '0';
	flag = a;
	getchar();
	if ((9 - (sum1 * 3 + sum2 - 1) % 10) == flag)
		printf("VALID");
	else
		printf("NOT VALID");
	return 0;
}
