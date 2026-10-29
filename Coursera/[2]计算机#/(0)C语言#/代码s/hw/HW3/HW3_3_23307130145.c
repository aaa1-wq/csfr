#include<stdio.h>
#include<math.h>
/*
	s1：输入三对实数，计算三条边的长度
	s2：判断是否为直角三角形，若能则标记 
	s3：判断是否能够成三角形
	s4：判断是否为等腰三角形
	s5：判断是否为等边三角形
	s6：输出结果
*/ 
int main()
{
	double x1, x2, x3, y1, y2, y3, a, b, c, m, n, q, temp;
	int flag = 0;
	printf("Enter 3 couples of coordinates: ");
	scanf("(%lf,%lf)(%lf,%lf)(%lf,%lf)", &x1, &y1, &x2, &y2, &x3, &y3);
	m = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
	n = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2);
	q = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3);
	if (fabs(m + n - q) < 1e-6 || fabs(m + q - n) < 1e-6 || fabs(q + n - m) < 1e-6)
		flag = 1;
	a = sqrt(m);
	b = sqrt(n);
	c = sqrt(q);
	if (!(a + b - c > 1e-6&& a + c - b > 1e-6 && b + c - a > 1e-6))
		printf("Can not make a triangle");
	else if (fabs(a - b) < 1e-6 || fabs(c - b) < 1e-6 || fabs(a - c) < 1e-6)
	{
		if (fabs(a - b) < 1e-6 && fabs(a - c) < 1e-6)
			printf("Equilateral triangle");
		else if (flag == 1)
			printf("Isosceles right triangle");
		else
			printf("Isosceles triangle");
	}
	else if (flag == 1)
		printf("Right triangle");
	else
		printf("Triangle");
	return 0;
}
