#include<stdio.h>
int main()
{
	int num, m, d, y;
	float price;
	printf("Enter item number: ");
	scanf("%d", &num);
	printf("Enter unit price: ");
	scanf("%f", &price);
	printf("Enter purchase date (mm/dd/yyyy): ");
	scanf("%d/%d/%d", &m, &d, &y);
	printf("Item\tUnit\t\tPurchase\t\t\n");
	printf("\tPrice\t\tDate\t\t\n");
	printf("%-d\t$%10.2f\t%d%02d%02d\n", num, price, y, m, d);
	return 0;
}
