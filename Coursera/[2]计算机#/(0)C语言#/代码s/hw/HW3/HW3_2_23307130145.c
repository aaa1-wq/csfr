#include<stdio.h>
int main()
{
	int a, b, c, d, l, s;
	printf("Enter 4 integers: ");
	scanf("%d %d %d %d", &a, &b, &c, &d);
	l = a > b ? a : b;
	l = l > c ? l : c;
	l = l > d ? l : d;
	s = a < b ? a : b;
	s = s < c ? s : c;
	s = s < d ? s : d;
	printf("Largest: %d\n", l);
	printf("Smallest: %d\n", s);
	return 0;
}
