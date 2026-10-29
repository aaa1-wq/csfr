/*	File:冒泡排序的基本算法	*/

#include <stdio.h>
#include <stdlib.h>
#define N 7
void swap2(short *x, short *y)
{
	short t;
	t = *x;
	*x = *y;
	*y = t;
}
void bubble1(short a[], short n)
{
	int i, j;
	for(i=n-1; i>0; i--)			/* 需要循环n-1 次			*/
	for(j=0; j<i; j++) 				/* 每次循环需要比较 i-1 次	*/
		if(a[j] > a[j+1])
			swap2(&a[j], &a[j+1]);	/* 交换a[j]和a[j+1]			*/
}

void main()
{
	short a[N], j;
	printf("input n and array ");
	for(j=0; j<N; j++)
		scanf("%hd", &a[j]);
	bubble1(a, N);
	for(j=0; j<N; j++)
		printf("%hd%c", a[j], (j+1)%8 ? ' ' : '\n');
	printf("\n");
}
/*
input n and array 7
8 4 3 6 9 2 7
2 3 4 6 7 8 9
*/
