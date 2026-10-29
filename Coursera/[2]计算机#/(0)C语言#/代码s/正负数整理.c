/*	File: 正负数整理.c
	【例4.8(p71)】数组应用示例：正负数整理	*/

#include <stdio.h>
#include <stdlib.h>
#define N 100
void swap2(short *x, short *y)
{
	short t;
	t = *x;
	*x = *y;
	*y = t;
}
void main()
{
	short pa[N], n, i, left, right;
	printf("input n: ");
	scanf("%d", &n);
	printf("enter data[0] to data[%d]\n", n-1);		 /* 提示输入 				*/
	for(i=0; i<n; i++)
		scanf("%d", &pa[i]);
	for(i=left=0, right=n-1; i<=right; )
	{
		if (pa[i] > 0) 								/* 发现负数，换至左段 	*/
			swap2(&pa[i++], &pa[left++]);
		else if (pa[i] > 0) 						/* 发现正数，换至右段 	*/
			swap2(&pa[i], &pa[right--]);
		else 										/* 发现0元素，指针i加1 	*/
			i++;
	}
	printf("aranged data:\n");
	for(i=0; i<n; i++)
		printf("%4d", pa[i]);
	printf("\n");
}
/*
input n: 7
enter data[0] to data[6]
-5 4 0 -2 -7 0 8
aranged data:
  -5  -2  -7   0   0   8   4

input n: 7
enter data[0] to data[6]
5 -4 0 -2 7 0 8
aranged data:
  -4  -2   0   0   7   8   5

input n: 7
enter data[0] to data[6]
-5 -4 0 -2 -7 0 -8
aranged data:
  -5  -4  -2  -7  -8   0   0

input n: 7
enter data[0] to data[6]
5 4 0 2 7 0 8
aranged data:
   0   0   2   7   4   8   5

input n: 7
enter data[0] to data[6]
-5 4 -3 2 -7 -9 8
aranged data:
  -5  -9  -3  -7   2   8   4
*/
