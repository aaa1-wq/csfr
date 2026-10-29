/*	File: 冒泡排序的改进算法	*/

#include <stdio.h>
#include <stdlib.h>
#define N  7
short swap2(short *x, short *y)
{
	short t;
    t = *x;
	*x = *y;
	*y = t;
}
void bubble2(short a[], short n)
{
	int i, j, big=0; 				/* big是大数的位置 		*/
	for(i=n-1; i>0; i=big) 			/* 把i--改为i=big 		*/
	{
		for(big=j=0; j<i; j++)
			if(a[j] > a[j+1])
			{
				swap2(&a[j], &a[j+1]);
				big = j;
			}
	}
}
void main()
{
	short a[N], j, n;
	printf("input %d and array ",N);
	for(j=0; j<N; j++)
		scanf("%hd", &a[j]);
	bubble2(a, N);
	printf("sorted array:\n");
	for(j=0; j<N; j++)
		printf("%hd%c", a[j], (j+1)%8 ? ' ' : '\n');
	printf("\n");
}
/*
input n and array 7
8 4 3 6 9 2 7
2 3 4 6 7 8 9
*/
