#include<stdio.h>
int gcd(int a, int b)
{
	static int n;
	n++;
	printf("Recursive layer %d: a = %d, b = %d\n", n, a, b);
	if (a == b)
		return a;
	else
		return a > b ? gcd(a - b, b) : gcd (a, b - a);
}
int main()
{
	int a, b;
	printf("/*** Find the greatest common divisor of two integers ***/\n");
	printf("Enter 2 integers: \n");
	scanf("%d %d", &a, &b);
	printf("The greatest common divisor of %d and %d is %d.", a, b, gcd(a, b));
	return 0;
}
