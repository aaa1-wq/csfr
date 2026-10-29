#include<stdio.h>
int main()
{
	int i, b, m, n, j;
	printf("* * * * * * * * * * * * * * * * * * * * *\n");
	printf("*                                       *\n");
	printf("* Conversion between decimal system and *\n");
	printf("* binary/octal system (1~256)           *\n");
	printf("*                                       *\n");
	printf("* * * * * * * * * * * * * * * * * * * * *\n");
	printf("Decimal    Binary    Octal\n");
	for (i = 1; i <= 256; i++)
	{
		m = n = i;
		int x[100];
		printf("%7d", i);
		j = 0;
		while (m)//转换10进制 
		{
			x[++j] = m % 2;
			m /= 2;
		}
		for (b = 1; b <= 10 - j; b++)//对齐 
			printf(" ");
		while (j)//输出 
			printf("%d", x[j--]);
		j = 0;
		while (n)//转换8进制 
		{
			x[++j] = n % 8;
			n /= 8;
		}
		for (b = 1; b <= 9 - j; b++)//对齐 
			printf(" ");
		while (j)//输出 
			printf("%d", x[j--]);
		printf("\n");
	}
	return 0;
}
