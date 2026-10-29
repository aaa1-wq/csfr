#include<stdio.h>
int step;
void nor(int n)
{
	printf("Recursion Level %d, parameter n = %d\n", ++step, n);
	if (n > 9)
		nor(n / 10);
	printf("%d\n", n % 10);
	printf("Recursion Level %d return.\n", step--);
	return;
}
void rev(int n)
{
	printf("Recursion Level %d, parameter n = %d\n", ++step, n);
	printf("%d\n", n % 10);
	if (n < 10)
		return ;
	rev(n / 10);
	printf("Recursion Level %d return.\n", step--);
}
int main()
{
	int x;
	printf("Enter a positive integer: ");
	scanf("%d", &x);
	printf("Output in normal order:\n");
	nor(x);
	printf("\n");
	printf("Output in reverse order:\n");
	rev(x);
	printf("Recursion Level %d return.\n", step);
	return 0;
}
