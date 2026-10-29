#include<stdio.h>
void output_header()
{
	char a[]={"Conversion between decimal system and\0"};
	char b[]={"binary/octal system (1~256)\0"};
	int i, n = strlen(a), m = strlen(b);
	
	printf("**");
	for (i = 1; i <= n; i++)
		printf("*");
	printf("**\n");
	
	printf("* ");
	for (i = 0; i < n; i++)
		printf(" ");
	printf(" *\n");
	
	printf("* %s *\n", a);
	
	printf("* %s", b);
	for (i = 0; i < n - m; i++)
		printf(" ");
	printf(" *\n");
	
	printf("* ");
	for (i = 0; i < n; i++)
		printf(" ");
	printf(" *\n");
	
	printf("**");
	for (i = 1; i <= n; i++)
		printf("*");
	printf("**\n\n");
	printf(" Decimal    Binary   Octal     hex\n");
}
void convert(int i, int k, int w)
{
	int b, m, j = 0, s;
	m = i;
	char x[100];
	if (x < 11)
	{
		while (m)
		{
			x[++j] = m % k + '0';
			m /= k;
		}
		for (b = 1; b <= w - j; b++)//¶ÔÆë 
			printf(" ");
		while (j)//Êä³ö 
			printf("%c", x[j--]);
	}
	else
	{
		while (m)
		{
			s = m % k;
			if (s < 10)
				x[++j] = s + '0';
			else
				x[++j] = s - 10 + 'A';
			m /= k;
		}
		for (b = 1; b <= w - j; b++)
			printf(" ");
		while (j)
			printf("%c", x[j--]);
	}
}
int main()
{
	int i;
	
	output_header();
	for (i = 1; i <= 256; i++){
		printf("%8d", i);
		convert(i, 2, 10);
		convert(i, 8, 8);
		convert(i, 16, 8);
		printf("\n");
	}
	
	return 0;
}
