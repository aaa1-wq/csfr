/*	File: 杨辉三角形.c
	【例6-14】打印杨辉三角形, 方案二：一维数组分段		*/

#include <stdio.h>
#include <stdlib.h>
#define N 100
void main()
{
	int i, j, n, *y[N];			/* 定义指针数组			*/
	int a[N*(N+1)/2];
	printf("Input n: ");
	scanf("%d", &n);
	for(y[0]=a, i=1; i<n; i++)	/* 一维数组分段			*/
		y[i] = y[i-1] + i;
	for(i=0; i<n; i++)		 	/* 生成所有数据			*/
	{
		y[i][0] = y[i][i] = 1;
		for(j=1; j<i; j++)
			y[i][j] = y[i-1][j-1] + y[i-1][j];
	}
	for(i=0; i<n; i++)			/* 按格式输出			*/
	{
		printf("%*c", 2*n-2*i, ' ');
		for(j=0; j<=i; j++)
			printf("%4d", y[i][j]);
		printf("\n");
	}
}
/*
Input n: 7
                 1
               1   1
             1   2   1
           1   3   3   1
         1   4   6   4   1
       1   5  10  10   5   1
     1   6  15  20  15   6   1

Input n: 10
                       1
                     1   1
                   1   2   1
                 1   3   3   1
               1   4   6   4   1
             1   5  10  10   5   1
           1   6  15  20  15   6   1
         1   7  21  35  35  21   7   1
       1   8  28  56  70  56  28   8   1
     1   9  36  84 126 126  84  36   9   1
*/
