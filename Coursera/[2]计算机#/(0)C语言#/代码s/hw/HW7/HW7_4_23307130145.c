#include<stdio.h>
#include<time.h>
void test(int n)
{
	char a[3][100] = {"Very good!\0", "Excellent!\0", "Keep up the good work!\0"};
	char b[3][100] = {"Sorry. Please try again.\0", "Wrong. Try once more.\0", "No. Keep trying.\0"};
	int k, l, h, s, d, flag = 0;
	if (n == 1)
		k = rand() % 10;
	else
	{
		h = 1 + rand() % 9;
		k = h * 10 + rand() % 10;
	}
	l = rand() % 10;
	s = rand() % 3;
	printf("请计算：\n");
	printf("%d×%d=", k, l);
	scanf("%d", &d);
	if (d == k * l)
		printf("%s\n", a[s]);
	else
	{
		printf("%s\n", b[s]);
		printf("%d×%d=%d\n", k, l, k * l);
	}
}
void menu()
{
	printf("请选择：\n");
	printf("        1. 一位数乘法\n");
	printf("        2. 二位数乘法\n"); 
	printf("        3. 退出小测试\n");
}
int main()
{
	srand(time(NULL));
	int n;
	printf("/***乘法小测试***/\n");
	while (1)
	{
		menu();
		scanf("%d", &n);
		if (n == 3)
			break;
		else
			test(n);
	}
	return 0;
}
