#include<stdio.h>
int main()
{
	int a, b, c, d, num;
	printf("Enter a 4-digit number: ");
	scanf("%4d", &num);
	a = num % 10;
	num /= 10;
	b = num % 10;
	num /= 10;
	c = num % 10;
	num /= 10;
	d = num % 10;
	num /= 10;
	printf("%d+%d+%d+%d=%d\n", d, c, b, a, a + b + c + d);
	return 0;
}
