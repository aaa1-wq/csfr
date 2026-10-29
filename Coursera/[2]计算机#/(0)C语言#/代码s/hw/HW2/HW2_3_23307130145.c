#include<stdio.h>
int main()
{
	float tota, rat, pa, a, b, c, d;
	printf("Enter amount of loan: ");
	scanf("%f", &tota);
	printf("Enter interest rate: ");
	scanf("%f", &rat);
	printf("Enter monthly payment: ");
	scanf("%f", &pa);
	a = tota + tota * rat /1200.0 - pa;
	b = a + a * rat /1200.0 - pa;
	c = b + b * rat /1200.0 - pa;
	printf("Balance remaining after 1st payment: $%.2f\n", a);
	printf("Balance remaining after 2nd payment: $%.2f\n", b);
	printf("Balance remaining after 3rd payment: $%.2f\n", c);
	return 0;
}
