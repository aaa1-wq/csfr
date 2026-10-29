#include<stdio.h>
int main()
{
	char s;
	int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0, i = 0, j = 0;
	printf("Enter an integer:\n");
	while ( scanf("%c", &s) )
	{
		if (s == '\n')
			break;
		else if (s == ' ')
			continue;
		else
			switch (s)
			{
				case '0' : a++; break;
				case '1' : b++; break;
				case '2' : c++; break;
				case '3' : d++; break;
				case '4' : e++; break;
				case '5' : f++; break;
				case '6' : g++; break;
				case '7' : h++; break;
				case '8' : i++; break;
				case '9' : j++; break;
			}
	}
	printf("Digit\tOccurrences\n");
	if (a)
		printf("0\t%d\n", a);
	if (b)
		printf("1\t%d\n", b);
	if (c)
		printf("2\t%d\n", c);
	if (d)
		printf("3\t%d\n", d);
	if (e)	
		printf("4\t%d\n", e);
	if (f)
		printf("5\t%d\n", f);
	if (g)
		printf("6\t%d\n", g);
	if (h)	
		printf("7\t%d\n", h);
	if (i)
		printf("8\t%d\n", i);
	if (j)
		printf("9\t%d\n", j);
	return 0;
}
