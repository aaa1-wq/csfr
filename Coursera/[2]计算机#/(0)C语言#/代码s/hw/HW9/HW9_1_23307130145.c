#include<stdio.h>
int main()
{
	char a[1005], x;
	int i = 0, sum1 = 0, sum2 = 0, m, low, high, flag = 0, sum3 = 0;
	printf("Enter some text:\n");
	do
	{
		x = getchar();
		a[++i] = x;
		if (! ( (x >= 'A' && x <= 'Z') || (x >= 'a' && x <= 'z') ))
		{
			if (flag == 1)
				sum3++;
			if (sum1 > sum2)
			{
				sum2 = sum1;
				low = m;
				high = i;
			}
			sum1 = 0;
			flag = 0;
			continue;
		}
		if (flag == 0)
		{
			flag = 1;
			m = i;
		}
		sum1++;
	}while (x != '\n');
	printf("There are %d words.\n", sum3);
	printf("The word of max length is: ");
	for (i = low; i < high; i++)
		printf("%c", a[i]);
	return 0;
}
