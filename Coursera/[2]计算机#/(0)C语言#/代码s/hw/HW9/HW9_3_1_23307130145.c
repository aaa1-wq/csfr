#include<stdio.h>
#define nl printf("\n")
void nor(int n)
{
	if (n > 9)
		nor(n / 10);
	printf("%d ", n % 10);
	return;
}
void rev(int n)
{
	printf("%d ", n % 10);
	if (n < 10)
		return;
	rev(n / 10);
}
int main()
{
	int x;
	printf("Enter a positive integer: ");
	scanf("%d", &x);
	printf("Output in normal order:\n");
	nor(x);
	nl;
	nl;
	printf("Output in reverse order:\n");
	rev(x);
	nl;
	nl;
	return 0;
}
